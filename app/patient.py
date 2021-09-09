from typing import Optional

from pydantic import BaseModel, EmailStr, Field
import datetime

class PatientSchema(BaseModel):
    fullname: str = Field(...)
    phoneNumber: int = Field(...)
    gender: str = Field(...)
    piority: bool = Field(...)
    startAppointmentTime: datetime.datetime = Field(...)
    durationOfAppointment: int = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "phoneNumber": 412323,
                "gender": "male",
                "piority": True,
                "startAppointmentTime": datetime.datetime(2018, 6, 1),
                "durationOfAppointment": 30,
            }
        }
class UpdatePatientModel(BaseModel):
    fullname: Optional[str]
    phoneNumber: Optional[int]
    gender: Optional[str]
    piority: Optional[bool]
    startAppointmentTime: Optional[datetime.datetime]
    durationOfAppointment: Optional[int]
    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Doe",
                "phoneNumber": 412323,
                "gender": "male",
                "piority": True,
                "startAppointmentTime": datetime.datetime(2018, 6, 1),
                "durationOfAppointment": 30,
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