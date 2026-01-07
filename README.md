🌩 Cloud Image Service

Scalable Cloud-Native Image Upload & Metadata Platform

A production-style backend for image upload, storage, and metadata management — built using AWS-style architecture and cloud-native patterns.

📌 Overview

Cloud Image Service is a scalable backend system designed to handle image uploads, cloud storage, and metadata persistence — similar to the core infrastructure used by platforms like Instagram, Google Photos, or Dropbox.

The system uses presigned URLs to allow clients to upload images directly to cloud storage (S3), ensuring:

High performance

Low backend load

Cost efficiency

Secure uploads

Metadata for each image (user, tags, time, etc.) is stored in DynamoDB, enabling fast filtering and queries.

The entire AWS environment is emulated locally using LocalStack, allowing full cloud-like behavior without AWS costs.

🏗 Architecture
Client
  |
  | (request upload)
  v
FastAPI (API Gateway + Lambda)
  |
  | → Generates Presigned URL
  v
Amazon S3 (Image Storage)

Metadata Flow:
FastAPI → DynamoDB


Key design choice:
Images never pass through the API server — they go directly from client → S3 using presigned URLs, just like in real cloud systems.

🛠 Tech Stack
Layer	Technology
API Layer	FastAPI (AWS Lambda style)
Storage	Amazon S3 (via LocalStack)
Database	Amazon DynamoDB
Cloud Emulator	LocalStack
Testing	Pytest + Moto
Language	Python 3.11
API Docs	Swagger / OpenAPI
🚀 Features

✔ Secure image upload using presigned URLs
✔ Metadata storage in DynamoDB
✔ List images with filters
✔ Download images securely
✔ Delete images and metadata
✔ Fully testable cloud stack
✔ Locally emulated AWS using Docker

📡 API Endpoints
1️⃣ Upload Image

POST /images/upload

Generates a presigned S3 upload URL and saves metadata.

Query Params

user_id (required)

tags (optional)

description (optional)

curl.exe -X POST "http://localhost:8000/images/upload?user_id=meghana&tags=selfie,cloud"


Response:

{
  "image_id": "uuid",
  "upload_url": "https://s3-presigned-url"
}

2️⃣ List Images

GET /images

Supports filtering by:

user_id

tag

curl.exe -X GET "http://localhost:8000/images?tag=selfie"

3️⃣ Download Image

GET /images/{image_id}/download

Returns a short-lived secure S3 download URL.

curl.exe -X GET "http://localhost:8000/images/{id}/download"

4️⃣ Delete Image

DELETE /images/{image_id}

Deletes both the S3 object and DynamoDB record.

curl.exe -X DELETE "http://localhost:8000/images/{id}"

🧪 Testing

The project includes both unit and integration tests.

Type	Tool
Unit Tests	Pytest + Moto
AWS Mocking	Moto
Cloud Emulation	LocalStack

Run all tests:

pytest

⚙️ Local Setup
1️⃣ Start AWS Services
docker-compose up -d


This launches:

S3

DynamoDB
inside LocalStack.

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run API
uvicorn app.main:app --reload


Access:

API → http://localhost:8000

Swagger → http://localhost:8000/docs

📂 Project Structure
cloud-image-service/
│
├── app/
│   ├── main.py        # API + business logic
│   ├── __init__.py
│   └── tests/
│       ├── test_upload.py
│       └── test_list.py
│
├── docker-compose.yml
├── requirements.txt
└── README.md

🔒 Cloud-Native Design Principles

Presigned URLs avoid Lambda size limits

Stateless API enables horizontal scaling

S3 + DynamoDB ensures durability

IAM-style access via signed URLs

Idempotent uploads supported

👤 Author

Meghana Shetty
📧 meghanashetty7227@gmail.com
