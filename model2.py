from pydantic import BaseModel
from typing import Optional, List
from enum import Enum
from uuid import uuid4, UUID

class Gender(str, Enum):
    male = "male"
    female = "female"
    
class Role(str, Enum):
    admin = "admin"
    student = "student"
    user = "user"

class User(BaseModel):
    id : Optional[UUID] = uuid4()
    first_name : str
    last_name : str
    middle_name : Optional[str] = None
    gender : Gender
    roles : List[Role]