📸 Cloud Image Service

A scalable, cloud-native image upload & metadata management system

🚀 Overview

This project is a production-style backend service for handling secure image uploads, cloud storage, and metadata management — similar to the image pipeline used in apps like Instagram, Google Photos, or Cloudinary.

It uses S3 presigned URLs so clients upload images directly to cloud storage without passing through the backend, making it:

Faster

Cheaper

More scalable

Metadata is stored in a NoSQL database (DynamoDB), allowing filtering, querying, and management of millions of images.

The entire cloud stack runs locally using LocalStack, giving a real AWS-like environment without cloud costs.

🧱 Architecture
Client (Browser / App)
        |
        | 1. Request upload URL
        ▼
FastAPI Backend
        |
        | 2. Generate presigned URL
        ▼
Amazon S3 (LocalStack)
        |
        | 3. Client uploads image directly
        ▼
DynamoDB (LocalStack)
        |
        | 4. Metadata stored & queried
        ▼
FastAPI APIs

🛠 Tech Stack
Layer	Technology
Language	Python 3.11
API Framework	FastAPI
Cloud Storage	Amazon S3 (via LocalStack)
Database	Amazon DynamoDB
Infrastructure	Docker + LocalStack
Testing	Pytest + Moto
⚙️ Setup Instructions
1️⃣ Install Requirements

Make sure you have:

Docker

Docker Compose

Python 3.11+

2️⃣ Start AWS Services Locally
docker-compose up -d


This starts:

S3

DynamoDB

3️⃣ Install Python Dependencies
pip install -r requirements.txt

4️⃣ Run the API
uvicorn app.main:app --reload


API will run at:

http://127.0.0.1:8000


Swagger UI:

http://127.0.0.1:8000/docs

📤 API Endpoints
Upload Image

POST /images/upload

Returns a presigned S3 upload URL and stores metadata.

Example:

curl -X POST "http://localhost:8000/images/upload?user_id=meghana&tags=selfie&description=test"

List Images

GET /images

Supports filters:

user_id

tag

Example:

curl "http://localhost:8000/images?user_id=meghana"

Download Image

GET /images/{image_id}/download

Returns a secure temporary S3 URL.

Delete Image

DELETE /images/{image_id}

Deletes both:

S3 file

DynamoDB metadata

🧪 Testing

This project includes fully isolated AWS-mocked tests using Moto.

Run:

pytest


It validates:

Presigned URL generation

DynamoDB storage

Image listing

📂 Project Structure
cloud_image_service/
├── app/
│   ├── main.py
│   ├── __init__.py
│   └── tests/
│       ├── test_upload.py
│       └── test_list.py
├── docker-compose.yml
├── requirements.txt
└── README.md

👩‍💻 Author

Meghana Shetty
📧 meghanashetty7227@gmail.com