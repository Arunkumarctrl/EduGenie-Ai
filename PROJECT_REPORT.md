# EDU GENIE – GOOGLE GEMINI POWERED LEARNING ASSISTANT

## 1. Abstract
EduGenie is an AI-powered learning assistant designed to support students during self-learning. The system provides question answering, simple topic explanations, paragraph summarization, automatic quiz generation, and structured learning recommendations. A FastAPI backend connects the web interface to AI modules, while the frontend allows students to interact with each service.

## 2. Objectives
- Provide quick academic question answering.
- Explain difficult topics in simple language.
- Summarize lengthy study material.
- Generate multiple-choice quizzes automatically.
- Recommend a progressive learning path for a selected topic.
- Provide a simple browser-based interface for students.

## 3. Modules
### Q&A Module
Accepts a student question and generates an answer using Gemini.

### Explanation Module
Explains a selected topic in student-friendly language. The implementation supports Gemini by default and an optional local LaMini-Flan-T5 model.

### Summarization Module
Converts long input into a shorter summary while preserving important ideas.

### Quiz Generation Module
Creates three multiple-choice questions with four options and an answer for each question.

### Learning Recommendation Module
Creates beginner, intermediate and advanced learning stages with topics, resources and adaptive learning tips.

## 4. System Architecture
User → Frontend → FastAPI Backend → Selected AI Module → Result → Frontend

## 5. Technologies
Python, FastAPI, HTML, CSS, JavaScript, Google Gemini API, optional Transformers and PyTorch.

## 6. Advantages
- One interface for multiple learning tasks.
- Reduces time spent searching and organizing study material.
- Generates interactive practice questions.
- Supports structured learning.

## 7. Limitations
- Gemini features require a valid API key and internet access.
- AI-generated content should be checked before academic submission.
- Local model mode needs additional memory and download time.

## 8. Future Enhancements
- Student login and progress tracking.
- Database for quiz scores.
- PDF/document upload and question answering.
- Voice input and text-to-speech.
- Personalized recommendations based on previous performance.
- Teacher/admin dashboard.

## 9. Conclusion
EduGenie combines a simple web interface with AI services to create a practical learning assistant. Its modular design makes it possible to add more educational features in future versions.
