 

# IdeaCraft – AI Project Idea Generator

IdeaCraft is an AI-powered project idea generator web app built using Flask and the Groq (OpenAI-compatible) API. It allows users to select their domain, skill level, and known technologies to get 5 personalized project ideas — and even download them as a PDF.


## Features

- User input for domain, skill level, and known technologies
- Generates 5 unique project ideas with titles and descriptions
- Option to download the generated ideas as a PDF
- Clean and responsive Flask-based user interface
- Dark mode support
- API keys managed securely via `.env` file


 ## Technologies Used

- **Flask**: Backend web framework in Python  
- **Groq API**: OpenAI-compatible large language model API  
- **HTML/CSS**: Frontend UI with custom styling  
- **Jinja2**: Template rendering engine used in Flask  
- **python-dotenv**: For managing environment variables  
- **fpdf / reportlab**: For generating PDF files
-  
## Tech Stack
### Frontend
  - HTML5
  - CSS3 (Dark UI)
  -JavaScript (Fetch API)
  -jsPDF (PDF generation)
### Backend
   -Python
   -Flask
   -Requests
   -python-dotenv

 ### AI Model
   -Groq API
   -Model: llama3-8b-8192

   ## Project Structure
   ```bash
 idea-craft/
│
├── app.py
├── .env
├── requirements.txt
│
├── templates/
│ └── index.html
│
├── static/
│ └── style.css
│
└── README.md    
 ```
## Setup Instructions  
### 1️ Clone the Repository
 ```
git clone https://github.com/your-username/project-idea-generator.git
cd project-idea-generator  ```
### 2️ Create Virtual Environment (Optional but Recommended)
 ```
python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate
 ```
### 3️ Install Dependencies
 ```
pip install -r requirements.txt
 ```
### 4️ Setup Environment Variables
Create a  ```.env  ``` file in the root directory:
 ```
GROQ_API_KEY=your_groq_api_key_here
 ```
### Run the Application
 ```
python app.py
 ```
Open your browser and go to:
     
 http://127.0.0.1:5000/
  ```
## How It Works


1. User enters topic, domain, skill level, and technologies
2. Frontend sends data to Flask `/generate` endpoint
3. Backend creates a structured AI prompt
4. Groq API generates project ideas
5. Ideas are displayed on UI and can be downloaded as PDF

##  Example Use Cases


- Students looking for **final year project ideas**
- Hackathon participants
- Beginners learning **GenAI + Flask**
- Resume-worthy AI project demonstration

  ##  Security Notes


- API key is stored securely using environment variables
- `.env` file should **not** be pushed to GitHub


##  Future Improvements


- User authentication
- Save/download ideas history
- Model selection option
- Deployment on Render / Railway

##  Author
**Nishu Bharti**
Project Name: **Idea Craft**
B.Tech CSE (AI Specialization)
