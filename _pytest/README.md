"# CrudFastAPIempleos" 
## Table of Contents
1. [Información General](#general-info)
2. [Tecnologías](#technologies)
3. [Installatión](#installation)
4. [FAQs](#faqs)
### General Info
***
API-REST elaborada con FastAPI y MongoDB, cuenta con servicio de registro de Aspirantes, Vacantes y realiza un Match si las condiciones en tiempo de 
de experiencia son superiores al 50%
### Screenshot
![Image text](https://i.ibb.co/ZBM9RZr/Screenshot-2022-09-06-at-16-53-53-Fast-API-para-la-creaci-n-y-gesti-n-de-aspirantes-a-cargos-compara.png)
![Image text](https://i.ibb.co/sJmQppV/Screenshot-2022-09-06-at-16-53-36-Screenshot.png)
## Technologies
***
A list of technologies used within the project:
* [Python](https://example.com): 3.9.13 
* [FastAPI](https://example.com)
* [MongoDb](https://example.com): lastest version
## Installation
***
Forma de instalacion Local 
```
$ git clone mario-barrientos-dev/CrudFastAPIempleos
$ conda activate (env de destino dentro de la carpeta)
$ uvicorn app:app --reload
```
Pueden realizarse pruebas de la API de manera libre siempre y cuando tengan las tecnologías instaladas

## FAQs
***

1. La ruta ('/') lleva a la parte inicial del CRUD
2. La ruta ('/users') lleva a la lista completa de Aspirantes
3. La ruta ('/users/{UserID}') lleva a la vista del aspirante indiviudal.
4. La ruta ('/vacancy') lleva a la lista de vacantes.
5. La ruta ('/vacancy/{VancancyID}') lleva a la vista del vacante indiviudal.
6. La ruta ('/recomendation/{UserID}') lleva a la sugerencia de la vacante que mejor aplica y si no es asi sugiere seguir intentando.
7. La ruta ('/users/{UserID}') y ('/vacancy/{VancancyID}') cuenta con servicio CRUD
* POST
* PUT
* DELETE
| Headline 1 in the tablehead | Headline 2 in the tablehead | Headline 3 in the tablehead |
|:--------------|:-------------:|--------------:|
| text-align left | text-align center | text-align right |
