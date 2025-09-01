
# FastAPI Demo - Products API

A simple FastAPI application demonstrating GET and POST endpoints for product management and inventory tracking.

## Features

- **GET /**: Welcome endpoint
- **GET /products/**: Get all products
- **GET /products/{product_id}**: Get a specific product by ID
- **POST /products/**: Create a new product

## Setup

1. **Create and activate virtual environment:**
   ```bash
   python -m venv myenv
   myenv\Scripts\activate.ps1  # Windows PowerShell
   ```

2. **Install dependencies:**
   ```bash
   pip install fastapi uvicorn
   ```

3. **Run the application:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**
   - API: http://localhost:8000
   - Interactive docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Project Structure

```
invoTrack/
├── main.py          # FastAPI application with endpoints
├── models.py        # Pydantic models
├── .gitignore       # Git ignore file
└── README.md        # This file
```

## API Usage Examples

### Get all products
```bash
curl http://localhost:8000/products/
```

### Get product by ID
```bash
curl http://localhost:8000/products/1
```

### Create a new product
```bash
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "searchValue": "Reddy"
}'
```

## Models

### Product
- `id`: integer
- `name`: string
- `description`: string
- `price`: float
- `quantity`: integer

## Built With

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation using Python type hints
- [Uvicorn](https://www.uvicorn.org/) - ASGI server implementation









Got it! You want to design an API endpoint (probably in your backend) where users can search for cases using State, Commission, and Search Value. Here’s a clear explanation and example implementation for a Node.js + Express backend:

1. API Design

Endpoint:

POST /case-search


Request Body (JSON):

{
  "state": "KARNATAKA",
  "commission": "Bangalore 1st & Rural Additional",
  "searchValue": "Reddy"
}


Alternatively, you can support query params for GET requests:

GET /case-search?state=KARNATAKA&commission=Bangalore 1st & Rural Additional&searchValue=Reddy


Response (JSON example):

[
  {
    "caseId": "1234",
    "title": "Reddy vs State",
    "state": "KARNATAKA",
    "commission": "Bangalore 1st & Rural Additional",
    "date": "2025-08-27"
  },
  ...
]



## project setup

1 pip install crawl4ai
2 crawl4ai-setup
3 python3 main.py
4 python3 main2.py
5 pip install fastapi uvicorn 
6 uvicorn main3:app --reload  Go to link and /docs
7 uvicorn main4:app --reload   in execution add url after that /sitemap.xmlp






# Crawl4AI Project

This project demonstrates how to set up and run different Python scripts and FastAPI applications using **Crawl4AI**.

---

## 🚀 Setup Instructions

### 1️⃣ Install Dependencies
```bash
pip install crawl4ai

2️⃣ Run Setup
crawl4ai-setup

3️⃣ Run main.py
python3 main.py

4️⃣ Run main2.py
python3 main2.py

🌐 Running FastAPI Applications
Install FastAPI and Uvicorn
pip install fastapi uvicorn

5️⃣ Run main3.py

Start the FastAPI server:

uvicorn main3:app --reload


Open your browser and go to:
👉 http://127.0.0.1:8000/docs

Here you can explore the API with Swagger UI.

6️⃣ Run main4.py

Start the FastAPI server:

uvicorn main4:app --reload


To test the execution, add a URL after /sitemap.xmlp, e.g.:
👉 http://127.0.0.1:8000/sitemap.xmlp?url=https://example.com

📌 Notes

Make sure Python 3.9+ is installed.

Use a virtual environment (venv) to avoid dependency conflicts.

Replace example.com with your target site when testing.

🛠️ Tech Stack

Python

Crawl4AI

FastAPI

Uvicorn
