☁️ Cloud Image Service
A cloud-native, scalable image storage & metadata platform
<p align="center"> <img src="https://img.shields.io/badge/FastAPI-0.110+-009688?style=for-the-badge&logo=fastapi"/> <img src="https://img.shields.io/badge/AWS-S3%20%7C%20DynamoDB-orange?style=for-the-badge&logo=amazonaws"/> <img src="https://img.shields.io/badge/LocalStack-Cloud%20Emulator-blue?style=for-the-badge"/> <img src="https://img.shields.io/badge/Python-3.11-yellow?style=for-the-badge&logo=python"/> </p>
🌟 What is this?

Cloud Image Service is a backend system that powers secure, high-performance image uploads just like Instagram, Google Photos, or Cloudinary.

Instead of sending large files through the server, it uses S3 Presigned URLs so users upload images directly to cloud storage — making it:

🚀 Faster

💸 Cheaper

📈 Infinitely scalable

All image metadata is stored in DynamoDB, allowing fast searching, filtering, and management.

This entire cloud system runs locally using LocalStack, giving you real AWS behavior without real AWS bills.

🧠 How it works
User App
   |
   | 1️⃣ Request upload URL
   ▼
FastAPI Server
   |
   | 2️⃣ Returns presigned S3 URL
   ▼
Amazon S3 (LocalStack)
   |
   | 3️⃣ Image uploaded directly
   ▼
DynamoDB (LocalStack)
   |
   | 4️⃣ Metadata stored
   ▼
FastAPI APIs → List / Download / Delete


This architecture is exactly how real cloud companies build image platforms.

🧰 Tech Stack
Layer	Tech
API	FastAPI
Cloud Storage	Amazon S3
Database	DynamoDB
Cloud Emulator	LocalStack
Testing	Pytest + Moto
Language	Python 3.11
⚙️ Setup in 60 seconds
1️⃣ Start cloud services
docker-compose up -d


This starts:

S3

DynamoDB

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Start the API
uvicorn app.main:app --reload


Now open:

http://127.0.0.1:8000/docs


and you get a full interactive API UI 🔥

🚀 What you can do
📤 Upload an image

Generates a secure cloud upload URL and saves metadata.

curl -X POST "http://localhost:8000/images/upload?user_id=meghana&tags=selfie&description=test"

📁 List images

Filter by user or tags.

curl "http://localhost:8000/images?user_id=meghana"

📥 Download image
curl "http://localhost:8000/images/{image_id}/download"


Returns a secure cloud link.

🗑️ Delete image
curl -X DELETE "http://localhost:8000/images/{image_id}"


Removes from both S3 and DynamoDB.

🧪 Tested like a real cloud system

This project uses Moto to mock AWS services and Pytest to validate:

Presigned URL generation

DynamoDB writes

API correctness

Run:

pytest

📂 Project Layout
cloud_image_service/
├── app/
│   ├── main.py
│   └── tests/
│       ├── test_upload.py
│       └── test_list.py
├── docker-compose.yml
├── requirements.txt
└── README.md

👩‍💻 Built by

Meghana Shetty
📧 meghanashetty7227@gmail.com