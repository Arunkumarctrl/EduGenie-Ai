# EduGenie - Google Gemini Powered Learning Assistant

EduGenie is a FastAPI-based AI learning assistant with five learning modules:

1. Q&A
2. Topic Explanation
3. Paragraph Summarization
4. Quiz Generation
5. Adaptive Learning Recommendations

## Technology
- Python
- FastAPI
- HTML/CSS/JavaScript
- Google Gemini API
- Optional Hugging Face Transformers + LaMini-Flan-T5 for local explanations

## Setup

### 1. Create a virtual environment
Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install packages
```bash
pip install -r requirements.txt
```

### 3. Configure Gemini
Copy `.env.example` to `.env` and put your Gemini API key in:
```text
GEMINI_API_KEY=your_key
```

Keep the key private. Do not upload `.env` to GitHub.

### 4. Run
```bash
uvicorn main:app --reload
```

Open:
http://127.0.0.1:8000

## API endpoints

- GET `/` - Web interface
- GET `/qa?question=...` - Q&A
- POST `/explain` - Explanation
- POST `/summarize` - Summarization
- POST `/quiz` - Quiz generation
- GET `/learn/recommendations?topic=...` - Learning path

## Demo inputs
Q&A: `Which is the largest ocean?`
Explanation: `Photosynthesis`
Summary: paste a paragraph about the Industrial Revolution
Quiz: `Pythagorean theorem`
Learning recommendation: `SQL`

## Important
The local Transformers explanation module is optional. By default the project uses Gemini for explanations so the demo is simpler and lighter.
