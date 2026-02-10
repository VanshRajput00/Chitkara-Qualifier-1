Gemini said
Here is the clean, professional version of your README.md without any comments. It is structured to highlight your compliance with the strict assessment criteria.

Chitkara University - Qualifier 1 (Class of 2027)
Project Overview
This repository contains the implementation of two REST APIs developed for the Qualifier 1. The project is built using Python and FastAPI, featuring external AI integration for intelligent, single-word responses.

Submission Details
Name: Vansh

Roll No: 2311981560

Email: vansh1560.be23@chitkarauniversity.edu.in

Deployment Platform: Render

Evaluation Compliance

Strict API Structure: All JSON responses follow the precise mandatory format.


Robust Validation: Implements Pydantic models for data integrity and boundary condition handling.


Graceful Error Handling: Provides appropriate HTTP status codes and ensures no server crashes.


Security Guardrails: Validates requests to ensure exactly one functional key is processed.

API Endpoints
1. GET /health
URL: https://chitkara-qualifier-1-9j22.onrender.com/health

Response Structure:

JSON
{
  "is_success": true,
  "official_email": "vansh1560.be23@chitkarauniversity.edu.in"
}


2. POST /bfhl
URL: https://chitkara-qualifier-1-9j22.onrender.com/bfhl

Method: POST

Header: Content-Type: application/json

Functional Keys and Logic
Key	Input	Output
fibonacci	Integer	
Fibonacci series 

prime	Integer array	
Prime numbers 

lcm	Integer array	
LCM value 

hcf	Integer array	
HCF value 

AI	Question string	
Single-word AI response 

Request Examples

Fibonacci: { "fibonacci": 7 } 


Prime: { "prime": [2, 4, 7] } 


LCM: { "lcm": [12, 18] } 


HCF: { "hcf": [24, 36] } 

AI: { "AI": "Capital of India?" } 

Response Structure
All successful responses follow this format:

JSON
{
    "is_success": true,
    "official_email": "vansh1560.be23@chitkarauniversity.edu.in",
    "data": <result>
}


Local Setup
Clone the repository:

Bash
git clone https://github.com/VanshRajput00/Chitkara-Qualifier-1
Install dependencies:

Bash
pip install -r requirements.txt
Run the server:

Bash
uvicorn main:app --reload
Deployment Configuration

Platform: Render 


Build Command: pip install -r requirements.txt 


Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
