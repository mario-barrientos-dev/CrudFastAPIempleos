from fastapi import FastAPI
from routes.recomendation import recomendation
from routes.user import user
from routes.vacancy import vacancy
from routes.recomendation import recomendation
from docs import tags_metadata
from fastapi import FastAPI
from fastapi import Request, status
from fastapi.responses import JSONResponse

app = FastAPI(
      title="FastAPI para la creación y gestión de aspirantes a cargos, comparar experiéncia y recomendar cargos",
    description="Esta es una API-REST con la cúal se podrá crear Aspirantes y Empresas y cotejar requerimientos",
    version="0.0.1",
    openapi_tags=tags_metadata
)

@app.exception_handler(Exception)
async def catch_exception_handler(request: Request, exc: Exception):
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "Un error ha ocurrido en la información ingresada, porfavor intente de nuevo"},
    )

@app.get('/')
def read_root():
    return {"Bienvenido": "Con esta API-REST se podrá administrar aplicantes, vacantes y sugerir cargos"}
app.include_router(user)
app.include_router(vacancy)
app.include_router(recomendation)
