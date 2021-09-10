from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

import patient as pt
import patientDB

router = APIRouter()

@router.post("/", response_description="Patient data added into the database")
async def add_student_data(patient: pt.PatientSchema = Body(...)):
    patient = jsonable_encoder(patient)
    new_patient = await patientDB.add_patient(patient)
    return pt.ResponseModel(new_patient, "Patient added successfully.")