import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

app = Flask(__name__)

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    topic = data.get('topic', '')
    domain = data.get('domain', '')
    skill = data.get('skill', '')
    technologies = data.get('technologies', '')

    if not topic:
        return jsonify({"idea": "Topic cannot be empty. Please provide a valid topic."})

    prompt = f"""Generate 5 innovative project ideas based on these details:
Topic: {topic}
Domain: {domain}
Skill Level: {skill}
Known Technologies: {technologies}

For each idea, provide:
Title:
Objective:
Technology Stack:

Format it clearly for each idea.
"""

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant generating unique project ideas."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(GROQ_API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        try:
            result = response.json()
            idea = result['choices'][0]['message']['content']
        except Exception as e:
            idea = "Error parsing the API response."
            print("Error parsing response:", e)
    else:
        idea = f"Error from API: {response.status_code} - {response.text}"

    return jsonify({"idea": idea})

if __name__ == '__main__':
    app.run(debug=True)





