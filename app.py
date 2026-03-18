from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List
import sqlite3
import os

app = FastAPI()

# Set up templates directory
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Database setup
DATABASE_URL = "sqlite:///./health_diagnosis.db"

def init_db():
    conn = sqlite3.connect('health_diagnosis.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS symptoms (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS diagnoses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        symptoms TEXT NOT NULL,
                        recommendation TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS resources (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        content TEXT NOT NULL
                    )''')
    # Seed data
    cursor.execute("INSERT INTO resources (title, content) VALUES (?, ?)",
                   ("Healthy Eating", "Tips for a balanced diet include...")
                  )
    conn.commit()
    conn.close()

init_db()

# Models
class Symptom(BaseModel):
    name: str

class DiagnosisRequest(BaseModel):
    symptoms: List[Symptom]

class ContactForm(BaseModel):
    name: str
    email: str
    message: str

# Routes
@app.get("/", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/diagnosis", response_class=HTMLResponse)
async def read_diagnosis(request: Request):
    return templates.TemplateResponse("diagnosis.html", {"request": request})

@app.get("/resources", response_class=HTMLResponse)
async def read_resources(request: Request):
    conn = sqlite3.connect('health_diagnosis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM resources")
    resources = cursor.fetchall()
    conn.close()
    return templates.TemplateResponse("resources.html", {"request": request, "resources": resources})

@app.get("/about", response_class=HTMLResponse)
async def read_about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def read_contact(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.post("/api/diagnosis")
async def create_diagnosis(diagnosis_request: DiagnosisRequest):
    # Mock AI logic
    recommendation = "Based on your symptoms, we recommend..."
    return {"recommendation": recommendation}

@app.get("/api/resources")
async def get_resources():
    conn = sqlite3.connect('health_diagnosis.db')
    cursor = conn.cursor()
    cursor.execute("SELECT title, content FROM resources")
    resources = cursor.fetchall()
    conn.close()
    return {"resources": resources}

@app.post("/api/contact")
async def submit_contact(contact_form: ContactForm):
    # Mock contact form submission logic
    return {"message": "Thank you for reaching out!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
