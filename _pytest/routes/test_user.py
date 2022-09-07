from fastapi import APIRouter, Response, status
from config.test_db import conn
from schemas.test_user import userAplication, usersAplications
from models.test_user import User
from uuid import uuid4
from fastapi.encoders import jsonable_encoder
from fastapi import Response
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT


user = APIRouter()

@user.get('/users', tags=["Aspirantes"])
def find_all_users():
    return usersAplications(conn.local.users.find())

@user.post('/users', response_model=User, tags=["Aspirantes"])
def cerate_users(user: User):
    user.UserId = str(uuid4())
    #En caso de querer acceder por email
    #email_ins = user.Email
    datos_compatibles = jsonable_encoder(user)
    id = conn.local.users.insert_one(datos_compatibles).inserted_id
    user = conn.local.users.find_one({"_id": id})
    return userAplication(user)


@user.get('/users/{UserId}', response_model=User, tags=["Aspirantes"])
def find_user(UserId: str):
    return userAplication(conn.local.users.find_one({"UserId": UserId}))


@user.put('/users/{UserId}', response_model=User, tags=["Aspirantes"])
def update_users(UserId: str, user: User):
    datos_compatibles = jsonable_encoder(user)
    conn.local.users.find_one_and_update({"UserId": UserId}, {"$set": dict(datos_compatibles)})
    return userAplication(conn.local.users.find_one({"UserId": UserId}))

@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=["Aspirantes"])
def delete_users(id: str):
    userAplication(conn.local.users.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)