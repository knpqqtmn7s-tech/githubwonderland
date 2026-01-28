
Proyecto.

Plataforma de blogs indie.

Nombre de la página. 

–Pendiente–

Descripcion
Proyecto sobre página web dedicada a la publicación y consulta de información acerca de videojuegos independientes (indie). Desarrolladores y aficionados podrán crear, publicar y difundir blogs en un espacio especializado para ellos. Se realizarán reseñas, análisis, noticias y experiencias u opiniones sobre este tipo de videojuegos. 

Stack

Vanilla HTML/CSS/Javascript: Debido a las restricciones establecidas por parte de la administración, el uso vanilla frontend fue elegido por su sencillez y simpleza.

FastAPI: Beneficioso debido al alto rendimiento y rapidez que ofrece al manejar filtros y cargar publicaciones. Tal como es mencionado en su página oficial es rápido a la par de Node.js gracias a Starlette y Pydantic además de ser intuitivo y fácil de aprender sobre la marcha.

Postgresql: Escalabilidad y flexibilidad. Es un sistema orientado a objetos por el cual se puede manejar los usuarios, sus roles y todas las publicaciones que puedan realizar de manera eficiente y estructurada.

RESTful API:La forma de comunicación estructurada, segura y escalable que se establece entre frontend y backend, elegida por la claridad de separación de cada parte del proyecto (Backend encargado de la lógica, Frontend la interfaz). 

Carpetas / directorio existente.
Existen dos carpetas principales dentro del proyecto:

frontEnd: Alberga las interfaces del usuario (páginas, formularios, botones, etc.) donde se puede enviar y recibir datos para las operaciones backend. Despliega la información disponible, las selecciones del usuario, renderización de respuestas, etc.

backEnd: Donde se procesan las solicitudes entrantes del front end, funcionamiento de la lógica de las operaciones. Es responsable de la definición de las reglas, el procesamiento de peticiones, respuestas JSON, conexión a la base de datos, etc.

Creación (paso a paso):

Entorno virtual.
python -m venv .venv

Activar
source .venv/bin/activate

Desactivar
Deactivate

Instalación de fastapi dentro del entorno
pip3 install “fastapi[standard]”

Creación del directorio de rutas y controlador

    mkdir app/api/routes
    mkdir app/api/controllers

Creacion y configuracion de main.py 
Crea el archivo “main.py” en el directorio “api”

Dentro de main.py importamos 

    from fastapi import FastAPI
    from app.api.routes.users import router as users_router

Creamos e incluimos router

    app = FastAPI()
    app.include_router(users_router)

Ruta default

@app.get("/")
def root():
   return {"message": "API running"}

Se crea la ruta “users.py” en el directorio “controllers”

Importamos controlador de usuarios

    from fastapi import APIRouter
    from app.api.controllers.usersCtrl import get_users
    router = APIRouter()
    
Definimos la ruta

    @router.get("/users")
    def users():
    return get_users()

Se crea archivo “usersCtrl.py” en el directorio “controllers”

Definimos el controlador

    def get_users():
    return {
        "message": "Lista de usuarios"
    }

Ejecuta el comando
    fastapi dev app/api/main.py    
