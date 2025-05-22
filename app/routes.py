from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from app.database import get_db
from datetime import datetime

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {
        "request": request,
        "now": datetime.now  # <- Aici e cheia
    })

# Dashboard
@router.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# Appointments
@router.get("/appointments", response_class=HTMLResponse)
def get_appointments(request: Request):
    with get_db() as db:
        appointments = db.execute("SELECT * FROM appointments").fetchall()
    return templates.TemplateResponse("appointments.html", {"request": request, "appointments": appointments})

@router.post("/appointments/add", response_class=HTMLResponse)
def add_appointment(date: str = Form(...), description: str = Form(...)):
    with get_db() as db:
        db.execute("INSERT INTO appointments (date, description) VALUES (?, ?)", (date, description))
        db.commit()
        appointments = db.execute("SELECT * FROM appointments").fetchall()
    return templates.TemplateResponse("appointments_list.html", {"request": {}, "appointments": appointments})

@router.delete("/appointments/{appointment_id}", response_class=HTMLResponse)
def delete_appointment(appointment_id: int):
    with get_db() as db:
        db.execute("DELETE FROM appointments WHERE id = ?", (appointment_id,))
        db.commit()
        appointments = db.execute("SELECT * FROM appointments").fetchall()
    return templates.TemplateResponse("appointments_list.html", {"request": {}, "appointments": appointments})

# Symptoms
@router.get("/symptoms", response_class=HTMLResponse)
def get_symptoms(request: Request):
    with get_db() as db:
        symptoms = db.execute("SELECT * FROM symptoms").fetchall()
    return templates.TemplateResponse("symptoms.html", {"request": request, "symptoms": symptoms})

@router.post("/symptoms/add", response_class=HTMLResponse)
def add_symptom(date: str = Form(...), symptom: str = Form(...)):
    with get_db() as db:
        db.execute("INSERT INTO symptoms (date, symptom) VALUES (?, ?)", (date, symptom))
        db.commit()
        symptoms = db.execute("SELECT * FROM symptoms").fetchall()
    return templates.TemplateResponse("symptoms_list.html", {"request": {}, "symptoms": symptoms})

@router.delete("/symptoms/{symptom_id}", response_class=HTMLResponse)
def delete_symptom(symptom_id: int):
    with get_db() as db:
        db.execute("DELETE FROM symptoms WHERE id = ?", (symptom_id,))
        db.commit()
        symptoms = db.execute("SELECT * FROM symptoms").fetchall()
    return templates.TemplateResponse("symptoms_list.html", {"request": {}, "symptoms": symptoms})

# Medications
@router.get("/medications", response_class=HTMLResponse)
def get_medications(request: Request):
    with get_db() as db:
        medications = db.execute("SELECT * FROM medications").fetchall()
    return templates.TemplateResponse("medications.html", {"request": request, "medications": medications})

@router.post("/medications/add", response_class=HTMLResponse)
def add_medication(name: str = Form(...), dosage: str = Form(...)):
    with get_db() as db:
        db.execute("INSERT INTO medications (name, dosage) VALUES (?, ?)", (name, dosage))
        db.commit()
        medications = db.execute("SELECT * FROM medications").fetchall()
    return templates.TemplateResponse("medications_list.html", {"request": {}, "medications": medications})

@router.delete("/medications/{medication_id}", response_class=HTMLResponse)
def delete_medication(medication_id: int):
    with get_db() as db:
        db.execute("DELETE FROM medications WHERE id = ?", (medication_id,))
        db.commit()
        medications = db.execute("SELECT * FROM medications").fetchall()
    return templates.TemplateResponse("medications_list.html", {"request": {}, "medications": medications})

