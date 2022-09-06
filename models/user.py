from lib2to3.pytree import Base
from pydantic import BaseModel
from typing import Union, Optional

class Skill(BaseModel):
    Python: int
    NoSql: int

class User(BaseModel):
    UserId: Optional[str]
    FirstName: str
    LastName: str       
    Email: str      
    YearsPreviousExperience: str
    Skills: Union[Skill, None] = None
    