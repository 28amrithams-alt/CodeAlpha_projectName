Public Help FAQ Chatbot 
Overview

The Public Help FAQ Chatbot is an AI-based question-answering system designed to assist the general public by resolving common doubts related to public safety, emergency services, healthcare guidance, women’s safety, and essential public facilities.

This chatbot can be deployed in public places, government portals, or kiosks to provide quick, reliable information and improve public safety awareness.

Features

Answers frequently asked public safety questions

Simple Natural Language Processing (NLP) logic

High-contrast UI (blue background with white text) for visibility

Web-based interface using Streamlit

Easy to extend with new FAQ datasets

Lightweight and beginner-friendly implementation

Technology Stack

Programming Language: Python

Frontend: Streamlit

Backend Logic: Rule-based NLP matching

Environment: Virtual Environment (venv)

Project Structure
FAQ Chatbot/
│
├── app.py              # Streamlit web application
├── chatbot.py          # Chatbot logic and matching function
├── data.py             # FAQ dataset
├── requirements.txt    # Required Python libraries
├── README.md           # Project documentation
└── venv/               # Virtual environment (optional)

Dataset Description

The dataset contains predefined questions (patterns) and answers (responses) related to:

Emergency services

Medical help

Public safety

Women safety

Travel and public assistance

The chatbot matches user input with the closest relevant question and returns an appropriate response.

Installation & Setup
1. Clone the Repository
git clone https://github.com/your-username/faq-chatbot.git
cd faq-chatbot

2. Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate     # Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application
streamlit run app.py

How It Works

User enters a question in natural language.

The chatbot processes the input text.

It finds the best matching question from the dataset.

The corresponding response is displayed instantly.

Use Case

Public information kiosks

Government service portals

Emergency awareness systems

Educational safety platforms

Future Enhancements

Multi-language support (English + Malayalam)

Machine Learning–based intent classification

Voice input support

Chat history storage

Mobile app integration

Internship Context

This project was developed as part of an Artificial Intelligence Internship at CodeAlpha IT Solutions to demonstrate practical understanding of:

NLP fundamentals

Python application development

User-centric design

Real-world problem solving

