from fastapi import FastAPI
from sqlalchemy import create_engine, Column, String, Float, Text
from sqlalchemy.orm import declarative_base, sessionmaker
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Ключ API OMDb
API_KEY = os.environ.get("API_KEY")
# Username и password для подключения к базе данных
username = os.environ.get("POSTGRES_USER")
password = os.environ.get("POSTGRES_PASSWORD")
# Хост базы данных
host = os.environ.get("POSTGRES_HOST")
# Имя базы данных
dbname = os.environ.get("POSTGRES_DB")

app = FastAPI()

# Конфигурация базы данных PostgreSQL
DATABASE_URL = f"postgresql://{username}:{password}@{host}/{dbname}"  # Замените на свои данные

Base = declarative_base()

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Movie(Base):
    __tablename__ = "movies"
    id = Column(String, primary_key=True)
    title = Column(String)
    description = Column(Text)
    rating = Column(Float)
    poster = Column(String)

    def __init__(self, id, title, description, rating, poster):
        self.id = id
        self.title = title
        self.description = description
        self.rating = rating
        self.poster = poster

Base.metadata.create_all(engine)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.get("/movies/{title}")
def get_movie(title: str):

    # Запрос к API OMDb для получения информации о фильме
    url = f"http://www.omdbapi.com/?t={title}&apikey={API_KEY}"
    response = requests.get(url)
    if response.status_code != 200:
        return{"message": "Ошибка с подключением к API"}
    movie_data = response.json()
    if movie_data["Response"] == "False":
        return {"message": "Movie not found"}

    # Извлечение нужных полей из полученных данных
    id = movie_data["imdbID"]
    title = movie_data["Title"]
    description = movie_data["Plot"]
    rating = float(movie_data["imdbRating"])
    poster = movie_data["Poster"]

    # Создание объекта фильма
    movie = Movie(id=id, title=title, description=description, rating=rating, poster=poster)

    # Добавление записи в базу данных если не существует
    db = SessionLocal()
    movie_exists = db.query(Movie).filter(Movie.id == id).first()
    if movie_exists:
        return {"message": "Movie already exists"}
    db.add(movie)
    db.commit()
    db.refresh(movie)
    db.close()

    return movie

@app.get("/movies")
def get_movies():
    # Получение всех записей из базы данных
    db = SessionLocal()
    movies = db.query(Movie).all()
    db.close()

    return movies

@app.delete("/movies/{id}")
def delete_movie(id: str):
    # Удаление записи из базы данных
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == id).first()
    if not movie:
        return {"message": "Movie does not exist"}
    db.delete(movie)
    db.commit()
    db.close()

    return {"message": "Movie deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)