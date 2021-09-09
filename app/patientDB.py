import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://kudo313:kudo_321@cluster1.mza5o.mongodb.net/test"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.hospitals

patient_collection = database.get_collection("patient")

def patient_helper(patient) -> dict:
    return {
        "id": str(patient["_id"]),
        "fullname": patient["fullname"],
        "gender": patient["gender"],
        "phoneNumber": str(patient["phoneNumber"]),
        "piority": patient["piority"],
        "startAppointmentTime": str(patient["startAppointmentTime"]),
        "durationOfAppointment": str(patient["durationOfAppointment"]),
    }

# Retrieve all patients present in the database
async def retrieve_patients():
    patients = []
    async for patient in patient_collection.find():
        patients.append(patient_helper(patient))
    return patients


# Add a new patient into to the database
async def add_patient(patient_data: dict) -> dict:
    patients = await patient_collection.insert_one(patient_data)
    new_patient = await patient_collection.find_one({"_id": patients.inserted_id})
    return patient_helper(new_patient)


# Retrieve a patient with a matching ID
async def retrieve_patient(id: str) -> dict:
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if patient:
        return patient_collection(patient)


# Update a patient with a matching ID
async def update_patient(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if patient:
        updated_patient = await patient_collection.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_patient:
            return True
        return False


# Delete a student from the database
async def delete_patient(id: str):
    patient = await patient_collection.find_one({"_id": ObjectId(id)})
    if patient:
        await patient_collection.delete_one({"_id": ObjectId(id)})
        return True