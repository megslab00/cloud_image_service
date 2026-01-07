Cloud-Based Image Upload & Metadata Service
📌 Project Overview
This project is a scalable, cloud-native image management service developed as part of the UNLOADIN internship assignment. The system supports secure image uploads, cloud storage, and metadata management using a NoSQL database, emulating a core module of applications like Instagram.

To ensure high performance and cost-efficiency, the service utilizes S3 Presigned URLs. This allows clients to upload and download images directly from S3, bypassing Lambda execution limits and reducing memory overhead.

🛠️ Tech Stack
Language: Python 3.11+

Framework: FastAPI (representing AWS API Gateway/Lambda logic)

Storage: Amazon S3

Database: Amazon DynamoDB (NoSQL)

Local Emulation: LocalStack

Testing: Pytest and Moto (for AWS mocking)

⚙️ Setup & Installation
1. Prerequisites
Ensure you have the following installed:

Docker and Docker Compose

Python 3.11+

2. Start Local Infrastructure
Run the following command to start S3 and DynamoDB locally via LocalStack:

Bash

docker-compose up -d
3. Install Dependencies
Bash

pip install -r requirements.txt
4. Run the Application
Bash

uvicorn app.main:app --reload
The API will be available at http://localhost:8000.

🚀 API Documentation & Usage
1. Upload Image (POST)
Endpoint: /images/upload Generates a presigned URL and saves metadata to DynamoDB.

Query Params: user_id, tags (optional), description (optional)

Bash

curl.exe -X POST "http://localhost:8000/images/upload?user_id=meghana&tags=test,cloud"
2. List Images (GET)
Endpoint: /images Supports filtering by user_id, tag, and date range.

Bash

# Filter by tag
curl.exe -X GET "http://localhost:8000/images?tag=cloud"
3. Download Image (GET)
Endpoint: /images/{image_id}/download Returns a short-lived presigned URL for secure image viewing or downloading.

Bash

curl.exe -X GET "http://localhost:8000/images/{id}/download"
4. Delete Image (DELETE)
Endpoint: /images/{image_id} Removes the image file from S3 and the metadata record from DynamoDB.

Bash

curl.exe -X DELETE "http://localhost:8000/images/{id}"
🧪 Testing
The project includes unit and integration tests to ensure reliability.

Unit Tests: Use moto to mock AWS services in-memory.

Integration Tests: Verify flows against the LocalStack environment.

To run all tests:

Bash

pytest
📂 Project Structure
Plaintext

cloud-image-service/
├── app/
│   ├── main.py          # FastAPI application & Business Logic
│   ├── __init__.py
│   └── tests/           # Unit and Integration tests
│       ├── test_list.py
│       └── test_upload.py
├── docker-compose.yml   # LocalStack configuration
├── requirements.txt     # Python dependencies
└── README.md            # Documentation
📞 Contact
For queries regarding this submission, please contact:

Developer: Meghanashetty7227@gmail.com

Submission To: Shricharan (shricharan@unloadin.com)