from pydantic import BaseModel
from typing import Union, Optional

class RequiredSkill(BaseModel):
    Python: int
    NoSql: int

class Vacancy(BaseModel):
    VacancyId: Optional[str]
    PositionName: str
    CompanyName: str       
    Salary: str      
    Currency: str
    VacancyLink: str
    RequiredSkills: Union[RequiredSkill, None] = None
    