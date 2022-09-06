from fastapi import APIRouter
from config.db import conn
from fastapi import APIRouter
from config.db import conn
from schemas.vacancy import vacanciesUp

recomendation = APIRouter()

@recomendation.get('/recomendation/{UserId}', tags=["Recomendacion de empleo"])
def recomendation_job(UserId: str):
    user_job = conn.local.users.find_one({"UserId": UserId})
    skill_python = user_job["Skills"]["Python"]
    skill_NoSQL = user_job["Skills"]["NoSql"]
    vacancies = vacanciesUp(conn.local.vacancy.find())
    
    for vacancy in vacancies:
        if 'RequiredSkills' in vacancy:
            p_skill = (vacancy['RequiredSkills']['Python'])
            n_skill = (vacancy['RequiredSkills']['NoSql'])  
            if (skill_python/p_skill>= 0.5 and skill_NoSQL/n_skill>=0.5):
                print ("tu trabajo recomendado es: ", vacancy['PositionName'])
                return ("tu trabajo recomendado es: ", vacancy['PositionName'])
            else:
                print ("sigue intentando")
                return ("sigue intentando")
        else:
            print('Esta clave no existe')
            return('Esta clave no existe')

    
             
        