from fastapi import FastAPI
from fastapi.responses  import HTMLResponse, JSONResponse
from pydantic import BaseModel
from jwt_manager import create_token
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router

app = FastAPI()
app.title = "Mi aplicación con fast API"
app.version = "1.0"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    email: str
    password: str

@app.get('/', tags=['home'])
def message():
    return HTMLResponse("<h1>Hello World!</h1>")

@app.post('/login', tags=['auth'])
def login(user: User):
    if user.email == "omarpava3@gmail.com" and user.password == "admin":
        token:str = create_token( user.dict() )
        return JSONResponse(
            content=token,
            status_code=200
        )