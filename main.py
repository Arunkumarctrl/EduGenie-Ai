import os
from typing import Optional
from fastapi import FastAPI, Request, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv

from gemini_module import (
    answer_question_with_gemini,
    summarize_text,
    generate_quiz,
    get_learning_recommendations,
)
from explanation_module import explain_topic

load_dotenv()

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/qa")
async def answer_question(question: str = Query(..., min_length=1)):
    try:
        return {"answer": answer_question_with_gemini(question)}
    except Exception as e:
        return JSONResponse(
            content={"error": f"Unable to answer question: {str(e)}"},
            status_code=500,
        )


@app.post("/explain")
async def explain_api(request: Request):
    data = await request.json()
    topic = data.get("topic", "").strip()
    if not topic:
        return JSONResponse(
            content={"error": "Please provide a topic."}, status_code=400
        )
    try:
        return {"topic": topic, "explanation": explain_topic(topic)}
    except Exception as e:
        return JSONResponse(
            content={"error": f"Unable to generate explanation: {str(e)}"},
            status_code=500,
        )


@app.post("/summarize")
async def summarize_api(request: Request):
    data = await request.json()
    text = data.get("text", "").strip()
    if not text:
        return JSONResponse(
            content={"error": "Please provide text to summarize."}, status_code=400
        )
    try:
        return {"summary": summarize_text(text)}
    except Exception as e:
        return JSONResponse(
            content={"error": f"Unable to summarize text: {str(e)}"},
            status_code=500,
        )


@app.post("/quiz")
async def quiz_api(request: Request):
    data = await request.json()
    text = data.get("text", "").strip()
    if not text:
        return JSONResponse(
            content={"error": "Please provide text for quiz."}, status_code=400
        )
    try:
        return {"quiz": generate_quiz(text)}
    except Exception as e:
        return JSONResponse(
            content={"error": f"Unable to generate quiz: {str(e)}"},
            status_code=500,
        )


@app.get("/learn/recommendations")
async def learning_recommendation_api(topic: str = Query(..., min_length=1)):
    try:
        return {
            "topic": topic,
            "recommendation": get_learning_recommendations(topic),
        }
    except Exception as e:
        return JSONResponse(
            content={"error": f"Unable to generate learning path: {str(e)}"},
            status_code=500,
        )
