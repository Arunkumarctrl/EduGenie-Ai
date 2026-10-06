import json
import os
import re
from google import genai
from google.genai import types

MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def _client():
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is not configured. Add it to the .env file."
        )
    return genai.Client(api_key=api_key)


def _generate(prompt: str) -> str:
    response = _client().models.generate_content(
        model=MODEL,
        contents=prompt,
        config=types.GenerateContentConfig(
            temperature=0.4,
            max_output_tokens=1200,
        ),
    )
    return (response.text or "").strip()


def answer_question_with_gemini(question: str) -> str:
    prompt = f"""
You are EduGenie, a friendly AI tutor.
Answer the student's question accurately and in simple language.
If the question is academic, include a short explanation and an example when useful.
Student question:
{question}
"""
    return _generate(prompt)


def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following passage in simple student-friendly language.
Keep the important ideas, remove repetition, and use a short paragraph or bullet points.

PASSAGE:
{text}
"""
    return _generate(prompt)


def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
You are an AI tutor. Create a structured learning path for:
{topic}

Include:
1. Beginner level: key concepts, approximate time, resources.
2. Intermediate level: key concepts, approximate time, resources.
3. Advanced level: key concepts, approximate time, resources.
4. Adaptive learning tips.

Keep it practical and easy for a college student to follow.
"""
    return _generate(prompt)


def _extract_json(text: str):
    text = re.sub(r"```(?:json)?", "", text, flags=re.I).replace("```", "").strip()
    match = re.search(r"\[.*\]", text, flags=re.S)
    if not match:
        raise ValueError("Gemini did not return valid quiz JSON.")
    return json.loads(match.group(0))


def generate_quiz(text: str) -> list:
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage/topic below.

Return ONLY valid JSON in this exact structure:
[
  {{
    "question": "Question text",
    "options": ["Option 1", "Option 2", "Option 3", "Option 4"],
    "answer": "Option 1"
  }}
]

Rules:
- Exactly 4 options per question.
- The answer must exactly match one option.
- Questions should test understanding, not trivia.
- No markdown.

PASSAGE/TOPIC:
{text}
"""
    return _extract_json(_generate(prompt))
