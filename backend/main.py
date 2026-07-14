from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from backend.ai import ask_gemini

app = FastAPI(title="EduGenie")

# Static Files
app.mount("/static", StaticFiles(directory="static"), name="static")

# HTML Templates
templates = Jinja2Templates(directory="templates")


# ---------------- HOME PAGE ---------------- #

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


# ---------------- EXPLAIN ---------------- #

@app.get("/explain")
async def explain(topic: str):

    prompt = f"""
    Explain the following topic in simple language for students.

    Topic: {topic}

    Format:
    1. Definition
    2. Explanation
    3. Example
    """

    response = ask_gemini(prompt)

    return {
        "task": "Explain",
        "topic": topic,
        "response": response
    }


# ---------------- QUESTION ANSWERING ---------------- #

@app.get("/qa")
async def qa(question: str):

    response = ask_gemini(question)

    return {
        "task": "Question Answering",
        "question": question,
        "response": response
    }


# ---------------- QUIZ GENERATION ---------------- #

@app.get("/quiz")
async def quiz(topic: str):

    prompt = f"""
    Generate 5 multiple choice questions on {topic}.

    Give:
    Question
    A)
    B)
    C)
    D)

    Mention the correct answer.
    """

    response = ask_gemini(prompt)

    return {
        "task": "Quiz",
        "topic": topic,
        "response": response
    }


# ---------------- SUMMARIZATION ---------------- #

@app.get("/summarize")
async def summarize(text: str):

    prompt = f"""
    Summarize the following text in simple points.

    {text}
    """

    response = ask_gemini(prompt)

    return {
        "task": "Summarization",
        "response": response
    }


# ---------------- LEARNING PATH ---------------- #

@app.get("/learn")
async def learn(topic: str):

    prompt = f"""
    Create a learning roadmap for {topic}.

    Include:
    Beginner
    Intermediate
    Advanced
    Recommended Resources
    """

    response = ask_gemini(prompt)

    return {
        "task": "Learning Path",
        "topic": topic,
        "response": response
    }