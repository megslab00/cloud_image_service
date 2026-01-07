import os
os.environ["AWS_ENDPOINT"] = ""

import boto3
import pytest
from moto import mock_aws
from fastapi.testclient import TestClient
from app.main import app, BUCKET, TABLE


client = TestClient(app)

@mock_aws
def test_upload_generates_presigned_url():
    # Setup mock S3
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket=BUCKET)

    # Setup mock DynamoDB
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    dynamodb.create_table(
        TableName=TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    response = client.post("/images/upload?user_id=meghana")

    assert response.status_code == 200
    data = response.json()

    assert "image_id" in data
    assert "upload_url" in data
    assert data["upload_url"].startswith("http")
