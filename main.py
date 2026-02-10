import math
import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import List, Union, Optional
from fastapi.responses import JSONResponse

app = FastAPI()

GEMINI_KEY = "AIzaSyAcvhv9F7mdFTkjzeAiL0LZn3B9i7KbzKQ"
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

OFFICIAL_EMAIL = "vansh1560.be23@chitkarauniversity.edu.in" 

class BFHLRequest(BaseModel):
    fibonacci: Optional[int] = None
    prime: Optional[List[int]] = None
    lcm: Optional[List[int]] = None
    hcf: Optional[List[int]] = None
    AI: Optional[str] = None

def get_fibonacci(n: int):
    if n <= 0: return []
    res = [0, 1]
    while len(res) < n:
        res.append(res[-1] + res[-2])
    return res[:n]

def get_primes(arr: List[int]):
    primes = []
    for n in arr:
        if n > 1:
            for i in range(2, int(math.sqrt(n)) + 1):
                if (n % i) == 0: break
            else: primes.append(n)
    return primes

@app.get("/health")
def health_check():
    return {
        "is_success": True,
        "official_email": OFFICIAL_EMAIL
    }

@app.post("/bfhl")
async def process_bfhl(request: BFHLRequest):
    try:
        input_data = request.dict(exclude_none=True)
        if len(input_data) != 1:
            return JSONResponse(
                status_code=400, 
                content={"is_success": False, "official_email": OFFICIAL_EMAIL, "data": "Error: Exactly one key is required."}
            )
        key = list(input_data.keys())[0]
        val = input_data[key]
        result = None
        if key == "fibonacci":
            result = get_fibonacci(val)
        elif key == "prime":
            result = get_primes(val)
        elif key == "lcm":
            if not val: result = 0
            else:
                l = val[0]
                for i in val[1:]:
                    l = abs(l * i) // math.gcd(l, i)
                result = l
        elif key == "hcf":
            if not val: result = 0
            else:
                h = val[0]
                for i in val[1:]:
                    h = math.gcd(h, i)
                result = h
        elif key == "AI":
            prompt = f"Answer in strictly one word: {val}"
            response = model.generate_content(prompt)
            result = response.text.strip().split()[0].replace(".", "").replace(",", "")
        return {
            "is_success": True,
            "official_email": OFFICIAL_EMAIL,
            "data": result
        }
    except Exception as e:
        return JSONResponse(
            status_code=400,
            content={"is_success": False, "official_email": OFFICIAL_EMAIL, "error": str(e)}
        )
