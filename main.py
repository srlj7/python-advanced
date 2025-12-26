from fastapi import FastAPI, HTTPException
from typing import List
from API_Model import User, Gender, Role
from uuid import UUID
app = FastAPI()

database: List[User] = [
    User(id=UUID("690b7f0c-7e46-483d-911f-3581d9d8d88f"),
         first_name="Saif",
         middle_name="Asaad",
         last_name="Naeem",
         gender=Gender.male,
         roles=[Role.student]
    ),
    User(id=UUID("30265c27-1891-4b29-a797-71d1b9b7e27c"),
         first_name="Ziad",
         middle_name="Abdullah",
         last_name="Alrufay",
         gender=Gender.male,
         roles=[Role.admin]
         )
]

@app.get("/")
async def root():
    return {"message": "Hello saif asaad"}

@app.get("/api/v1/users")
async def get_users():
    return database

@app.post("/api/v1/users")
async def create_user(user: User):
    database.append(user)
    return {"id": user.id,
            "first_name": user.first_name,
            "middle_name": user.middle_name,
            "last_name": user.last_name,
            "gender": user.gender,
            "roles": user.roles}
    raise HTTPException(
        status_code=404,
        detail="User not found"
    )