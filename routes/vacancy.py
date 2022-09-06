from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.vacancy import vacancyUp, vacanciesUp
from models.vacancy import Vacancy
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi import Response
from starlette.status import HTTP_204_NO_CONTENT

vacancy = APIRouter()

@vacancy.get('/vacancy', tags=["Vacantes"])
def find_all_vacancies():
    return vacanciesUp(conn.local.vacancy.find())

@vacancy.post('/vacancy', response_model=Vacancy, tags=["Vacantes"])
def cerate_vacancy(vacancy: Vacancy):
    vacancy.VacancyId = str(uuid4())
    #En caso de querer acceder por email
    #email_ins = user.Email
    datos_compatibles = jsonable_encoder(vacancy)
    id = conn.local.vacancy.insert_one(datos_compatibles).inserted_id
    vacancy = conn.local.vacancy.find_one({"_id": id})
    return vacancyUp(vacancy)

@vacancy.get('/vacancy/{VacancyId}', response_model=Vacancy, tags=["Vacantes"])
def find_vacancy(VacancyId: str):
    return vacancyUp(conn.local.vacancy.find_one({"VacancyId": VacancyId}))

@vacancy.put('/vacancy/{VacancyId}', response_model=Vacancy, tags=["Vacantes"])
def update_vacancy(VacancyId: str, vacancy: Vacancy):
    datos_compatibles = jsonable_encoder(vacancy)
    conn.local.vacancy.find_one_and_update({"VacancyId": VacancyId}, {"$set": dict(datos_compatibles)})
    return vacancyUp(conn.local.vacancy.find_one({"VacancyId": VacancyId}))

@vacancy.delete('/vacancy/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Vacantes"])
def delete_vacancy(id: str):
    vacancyUp(conn.local.vacancy.find_one_and_delete({"_id": id}))
    return Response(status_code=HTTP_204_NO_CONTENT)