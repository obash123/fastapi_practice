from uuid import uuid4, UUID
from fastapi import FastAPI, HTTPException
from model2 import User, Gender, Role
from typing import List


app = FastAPI()

db2 :List[User] = [

]

db : List[User] = [
    User(
        id="212a6a34-ad1f-4a8d-91c7-af5b93cb5207", 
         first_name="Obasola", 
         last_name="Obayemi",
         gender=Gender.male,
         roles= [Role.student]
    ),
    User(
        id="e4fec588-05b9-4a64-aeea-6df9e4102deb", 
         first_name="Gbemileke", 
         last_name="Osinaike",
         gender=Gender.male,
         roles= [Role.admin, Role.user]
    ),
    User(
        id='bd05644e-21c9-41dd-b398-a1fee15da33c', 
         first_name="Femi", 
         last_name="Obakin",
         gender=Gender.male,
         roles= [Role.student]
    ),
    User(
        id='25ae729a-21ae-41ad-b828-6686e5ddceaf', 
         first_name="Joladale", 
         last_name="Alfonso",
         gender=Gender.male,
         roles= [Role.student]
    ),    
]

@app.get("/")
def root():
    return {"Hello":"world"}

@app.get("/api/users")
async def get_users():
    return db

@app.get("/api/get_student_and_admin_numbers")
async def get_student_and_admin_numbers():
    total_students = 0
    total_admins = 0
    for user in db:
        if Role.student in user.roles:
            total_students += 1
        elif Role.admin in user.roles:
            total_admins +=  1
    return {"total_students": total_students, "total_admins": total_admins}



@app.get("/api/get_user_by_user_id/{user_id}//")
async def get_user_by_user_id(users_id: UUID):
    for user in db:
        if user.id == users_id:
            return user
    raise HTTPException(status_code=404, detail="ID not found")


@app.get("/api/get_user_by_model_field_names/")
async def get_user_by_model_field_names(model_field: str):
    for existing_user in db:
        if existing_user.first_name == model_field or existing_user.last_name == model_field or existing_user.middle_name == model_field or existing_user.gender == model_field:
            return existing_user
    raise HTTPException(status_code=404, detail="User not found")    

@app.get("/api/get_total_number_of_users")
async def get_total_number_of_users():
    return db.count()

@app.delete("/api/delete_user/{user_id}/")
async def delete_user(user_id: UUID):
    for index, user in enumerate(db):
        if user.id == user_id:
            del db[index]
            return {"message": f"User {user_id} deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@app.post("/api/create_user", response_model=User)
async def create_user(user: User):
    for existing_user in db:
        if existing_user.gender == user.gender and (existing_user.first_name == user.first_name 
                                                    or existing_user.last_name == user.last_name):
            raise HTTPException(status_code=404, detail="You can have the same name first name or last name")
    db.append(user)
    return user

@app.post("/api/create_user_list", response_model= List[User])
async def create_user_list(users: List[User]):
    for user in users:
        db.append(user)
    return users

# write end to retrieve by guid,
# filter with the model field names
# return total count of all the users on the system
# create lists of user objects 