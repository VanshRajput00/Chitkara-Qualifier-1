# Chitkara University - Qualifier 1 (Class of 2027)

## Project Overview
This repository contains the implementation of two REST APIs developed for the **Chitkara Qualifier 1 (Feb 2026)**. The project is built using **Python** and **FastAPI**, featuring external **AI integration** via Google Gemini.

### Submission Details
- **Name:** Vansh
- **Roll No:** 2311981560
- **Email:** vansh1560.be23@chitkarauniversity.edu.in
- **Deployment Platform:** Render

---

## API Endpoints

### 1. GET /health
Checks the current status of the API and returns official identification.
- **URL:** `https://your-app-name.onrender.com/health`
- **Response Structure:**
  ```json
  {
    "is_success": true,
    "official_email": "vansh1560.be23@chitkarauniversity.edu.in"
  }
---

## API Endpoints

### 2. POST /bfhl
Processes input data for calculation or AI interactions.

- **URL:** `https://your-app-name.onrender.com/bfhl`
- **Method:** `POST`
- **Header:** `Content-Type: application/json`

#### Request Body (Select ONE key per request):

1. **Fibonacci Sequence:**
```json
{ "fibonacci": 8 }
```
*Returns the first 8 Fibonacci numbers.*

2. **Prime Numbers:**
```json
{ "prime": [10, 2, 13, 17, 4, 8] }
```
*Returns all prime numbers from the list.*

3. **LCM Calculation:**
```json
{ "lcm": [4, 6, 8] }
```
*Returns the Least Common Multiple of the numbers.*

4. **HCF Calculation:**
```json
{ "hcf": [12, 18, 24] }
```
*Returns the Highest Common Factor of the numbers.*

5. **AI Interaction:**
```json
{ "AI": "What is the capital of India?" }
```
*Returns a single-word AI-generated answer.*

## Response Structure
All successful responses follow this format:
```json
{
    "is_success": true,
    "official_email": "vansh1560.be23@chitkarauniversity.edu.in",
    "data": <result>
}
```

## How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server:**
   ```bash
   uvicorn main:app --reload
   ```

4. **Access the API:**
   - Health Check: `http://127.0.0.1:8000/health`
   - POST Request: `http://127.0.0.1:8000/bfhl` (Use Postman or Curl)

## Deployment

This project is configured for deployment on **Render**.
1. Push code to GitHub.
2. Link repository to Render Web Service.
3. Build Command: `pip install -r requirements.txt`
4. Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`