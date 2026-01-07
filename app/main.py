from fastapi import FastAPI, Query, Depends, HTTPException
import boto3
import uuid
import datetime
import os

app = FastAPI(title="Cloud Image Service")

# Config
REGION = "us-east-1"
BUCKET = "images-bucket"
TABLE = "images"

def get_aws_config():
    """Helper to return endpoint only if LocalStack is intended."""
    endpoint = os.getenv("AWS_ENDPOINT", "http://localhost:4566")
    # If endpoint is empty string or None, return None so Moto can intercept
    if not endpoint or endpoint.lower() == "none":
        return None
    return endpoint

def get_dynamodb():
    return boto3.resource(
        "dynamodb",
        region_name=REGION,
        endpoint_url=get_aws_config(),
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )

def get_s3():
    return boto3.client(
        "s3",
        region_name=REGION,
        endpoint_url=get_aws_config(),
        aws_access_key_id="test",
        aws_secret_access_key="test",
    )

def get_table(dynamodb=Depends(get_dynamodb)):
    return dynamodb.Table(TABLE)

@app.get("/")
def root():
    return {"status": "running"}

@app.post("/images/upload")
def upload_image(user_id: str, tags: str = "", description: str = "", 
                 table=Depends(get_table), s3=Depends(get_s3)):
    image_id = str(uuid.uuid4())
    s3_key = f"{user_id}/{image_id}"

    # Metadata for DynamoDB
    upload_time = datetime.datetime.utcnow().isoformat()

    url = s3.generate_presigned_url(
        "put_object",
        Params={"Bucket": BUCKET, "Key": s3_key, "ContentType": "image/jpeg"},
        ExpiresIn=3600,
    )

    table.put_item(
        Item={
            "image_id": image_id,
            "user_id": user_id,
            "s3_key": s3_key,
            "upload_time": upload_time,
            "tags": tags,
            "description": description,
        }
    )

    return {"image_id": image_id, "upload_url": url}

@app.get("/images")
def list_images(user_id: str = Query(None), tag: str = Query(None),
                start_date: str = Query(None), end_date: str = Query(None),
                table=Depends(get_table)):
    
    items = table.scan().get("Items", [])

    # Filter logic
    if user_id:
        items = [i for i in items if i["user_id"] == user_id]
    if tag:
        items = [i for i in items if tag in i.get("tags", "")]
    if start_date and end_date:
        items = [i for i in items if start_date <= i["upload_time"] <= end_date]

    return items

@app.get("/images/{image_id}/download")
def download_image(image_id: str, table=Depends(get_table), s3=Depends(get_s3)):
    item = table.get_item(Key={"image_id": image_id}).get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="Image not found")

    url = s3.generate_presigned_url(
        "get_object",
        Params={"Bucket": BUCKET, "Key": item["s3_key"]},
        ExpiresIn=3600,
    )
    return {"download_url": url}

@app.delete("/images/{image_id}")
def delete_image(image_id: str, table=Depends(get_table), s3=Depends(get_s3)):
    item = table.get_item(Key={"image_id": image_id}).get("Item")
    if not item:
        raise HTTPException(status_code=404, detail="Image not found")

    s3.delete_object(Bucket=BUCKET, Key=item["s3_key"])
    table.delete_item(Key={"image_id": image_id})

    return {"status": "deleted"}