import os
import boto3
import pytest
from moto import mock_aws
from fastapi.testclient import TestClient

# 1. SET ENV VARS BEFORE IMPORTING APP
os.environ["AWS_ENDPOINT"] = "" # Our new get_aws_config handles "" as None
os.environ["AWS_ACCESS_KEY_ID"] = "testing"
os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
os.environ["AWS_SECURITY_TOKEN"] = "testing"
os.environ["AWS_SESSION_TOKEN"] = "testing"
os.environ["AWS_DEFAULT_REGION"] = "us-east-1"

from app.main import app, TABLE

client = TestClient(app)

@mock_aws
def test_list_images():
    # Inside @mock_aws, everything is isolated and empty
    dynamodb = boto3.client("dynamodb", region_name="us-east-1")
    dynamodb.create_table(
        TableName=TABLE,
        KeySchema=[{"AttributeName": "image_id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "image_id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )

    table = boto3.resource("dynamodb", region_name="us-east-1").Table(TABLE)
    table.put_item(Item={
        "image_id": "123",
        "user_id": "meghana",
        "s3_key": "meghana/123",
        "tags": "selfie",
        "description": "test"
    })

    response = client.get("/images")

    assert response.status_code == 200
    
    assert len(response.json()) == 1