from fastapi import APIRouter, Path, Query, Depends, Request, HTTPException
from fastapi.responses  import JSONResponse
from fastapi.security import HTTPBearer
from pydantic import BaseModel, Field
from typing import Optional, List
from jwt_manager import create_token, validate_token
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder
from services.movie import MovieService

movie_router = APIRouter()

class JwtBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data['email'] != "omarpava3@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")

class Movie(BaseModel):
    id: Optional [int] = None
    title: str = Field(min_length = 1, max_length=35)
    overview: Optional [str] = Field(min_length = 1, max_length=35)
    year: Optional [int] = Field(le=2024)
    rating: Optional [float] = Field(ge=0, le=10)
    category:Optional [str] = Field(min_length = 5, max_length=35)


    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "Título por defecto",
                    "overview": "Descripción por defecto",
                    "year": 2022,
                    "rating": 0.0,
                    "category": "Categoría por defecto"
                }
            ]
        }
    }

@movie_router.get('/movies', tags=['movies'], response_model=List[Movie], status_code=200, dependencies=[Depends(JwtBearer())])
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@movie_router.get('/movies/{id}', tags=['movies'], response_model=List[Movie])
def get_movie(id:int  = Path( ge=0, le=2000)) -> List[Movie] :
    db = Session()
    result = MovieService(db).get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"status":"Movie not found"})
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@movie_router.get('/movies/', tags=['movies'], dependencies=[Depends(JwtBearer())])
def get_movies_by_category( category: str = Query( min_lenth=0, max_length=15 )):
    db = Session()
    result = MovieService(db).get_movie_by_category(category)
    return JSONResponse(status_code=200, content = jsonable_encoder(result))

@movie_router.post('/movies', tags=['movies'], response_model=dict, status_code = 201)
def create_movies(movie: Movie ) -> dict:
    db = Session()
    new_movie = MovieModel(**movie.dict())
    db.add( new_movie )
    db.commit()

    return JSONResponse(status_code = 201, content = {
        "message": "Movie created successfully"
    })

@movie_router.put('/movies/{id}', tags=['movies'])
def update_movies(id:int, movie : Movie):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"status":"Movie not found"})
    
    result.title = movie.title
    result.overview = movie.overview
    result.year = movie.year
    result.category = movie.category
    result.rating = movie.rating
    db.commit()
    return JSONResponse(status_code = 404, content ={"status":"Movie modified successfully"})


@movie_router.delete('/movies/{id}', tags=['movies'])
def delete_movies(id:int):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={"status":"Movie not found"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code = 200, content ={"status":"Movie deleted successfully"})
