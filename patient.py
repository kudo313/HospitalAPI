from typing import Optional

from pydantic import BaseModel, EmailStr, Field
import datetime

class PatientSchema(BaseModel):
    fullname: str = Field(...)
    phoneNumber: int = Field(...)
    gender: str = Field(...)
    piority: bool = Field(...)
    startAppointmentTime: float = Field(...)
    appointmentDate: str = Field(...)
    durationOfAppointment: float = Field(...)
    apartmentName: str = Field(...)
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "phoneNumber": 412323,
                "gender": "male",
                "piority": True,
                "startAppointmentTime": 9,
                "appointmentDate": datetime.datetime(2018, 6, 1).strftime("%m/%d/%Y"),
                "durationOfAppointment": 1,
                "apartmentName": "ngoai khoa",
            }
        }
class UpdatePatientModel(BaseModel):
    fullname: Optional[str]
    phoneNumber: Optional[int]
    gender: Optional[str]
    piority: Optional[bool]
    startAppointmentTime: Optional[float]
    appointmentDate: Optional[str]
    durationOfAppointment: Optional[float]
    apartmentName: Optional[str]
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "phoneNumber": 412323,
                "gender": "male",
                "piority": True,
                "startAppointmentTime": 9,
                "appointmentDate": datetime.datetime(2018, 6, 1).strftime("%m/%d/%Y"),
                "durationOfAppointment": 1,
                "apartmentName": "ngoai khoa",
            }
        }
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}