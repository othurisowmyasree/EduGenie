📚 EduGenie - AI Powered Educational Assistant

Overview

EduGenie is an AI-powered educational assistant developed using FastAPI, HTML, CSS, and Generative AI. It helps students understand concepts, answer questions, generate quizzes, summarize educational content, and receive personalized learning recommendations.

The application provides an easy-to-use interface where users can enter a topic or question, choose the required educational task, and instantly receive AI-generated responses.

------------------------------------------------------------

🚀 Features

• Intelligent Question Answering

• Simplified Concept Explanation

• AI-Powered Quiz Generation

• Educational Text Summarization

• Personalized Learning Path Recommendation

• Interactive Web Interface

------------------------------------------------------------

🛠 Technologies Used

Backend

• Python 3.10+

• FastAPI

• Uvicorn

Frontend

• HTML5

• CSS3

• JavaScript

AI

• Groq API

• Llama 3.3 70B Versatile

Other Libraries

• Jinja2

• python-dotenv

• Transformers

• Torch

------------------------------------------------------------

📂 Project Structure

EduGenie
│
├── backend
│   ├── ai.py
│   ├── main.py
│   └── __init__.py
│
├── static
│   └── style.css
│
├── templates
│   └── index.html
│
├── .env
├── .gitignore
├── README.md
└── requirements.txt

------------------------------------------------------------

⚙ Installation

1. Clone the Repository

git clone https://github.com/othurisowmyasree/EduGenie.git

2. Navigate to Project

cd EduGenie

3. Create Virtual Environment

python -m venv venv

4. Activate Virtual Environment

Windows

venv\Scripts\activate

Linux/macOS

source venv/bin/activate

5. Install Dependencies

pip install -r requirements.txt

6. Create .env File

GROQ_API_KEY=YOUR_API_KEY

7. Run the Project

python -m uvicorn backend.main:app --reload

------------------------------------------------------------

🌐 Open in Browser

http://127.0.0.1:8000

------------------------------------------------------------

🎯 Application Modules

📖 Concept Explanation

Explains any topic in simple language with examples.

❓ Question Answering

Answers educational questions accurately using AI.

📝 Quiz Generation

Creates topic-based multiple-choice quizzes.

📚 Text Summarization

Summarizes lengthy educational content into concise points.

🛣 Learning Path

Generates a personalized roadmap for learning a selected topic.

------------------------------------------------------------

💻 System Requirements

Hardware

• Intel i3 / i5 or above

• Minimum 4 GB RAM

• 10 GB Free Storage

• Internet Connection

Software

• Windows / Linux / macOS

• Python 3.10+

• FastAPI

• Visual Studio Code

------------------------------------------------------------

🔮 Future Enhancements

• User Authentication

• Database Integration

• PDF Upload and Summarization

• Voice-Based Learning Assistant

• Multi-language Support

• Chat History

• Student Progress Tracking

------------------------------------------------------------

👨‍💻 Developed By

OTHURI SOWMYA SREE

B.Tech Student

------------------------------------------------------------

📄 License

This project is developed for educational and learning purposes.
