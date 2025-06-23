import os
import google.generativeai as genai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize FastAPI app
app = FastAPI()

# Define request model
class ExplainRequest(BaseModel):
    topic: str
    depth: int

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

# Define prompt templates
# Task: make automate prompt dept and scaleable level later.
depth_prompts = {
    1: "Explain this concept in simple terms.",
    2: "Explain this concept in detail with examples.",
    3: "Explain this concept with advanced technical details.",
    4: "Provide an in-depth academic explanation of this concept.",
}

# Generate explanation
@app.post("/explain")
async def explain(req: ExplainRequest):
    prompt = f"Topic: {req.topic}\n{depth_prompts.get(req.depth, 'Explain this concept in simple terms.')}"
    try:
        response = model.generate_content(prompt)
        return {"response": response.text.strip()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
