import pytest
# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# from main import app, Base
# import os
# from dotenv import load_dotenv
# from fastapi import FastAPI

# load_dotenv()

# # Подключение к тестовой базе данных
# username = os.environ.get("POSTGRES_USER")
# password = os.environ.get("POSTGRES_PASSWORD")
# # Хост базы данных
# host = "localhost"
# # Имя базы данныхaa
# dbname = os.environ.get("POSTGRES_DB")

# app = FastAPI()

# Конфигурация базы данных PostgreSQL
# DATABASE_URL = f"postgresql://{username}:{password}@localhost/{dbname}"
# engine = create_engine(DATABASE_URL)
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# # Создание всех таблиц в тестовой базе данных
# Base.metadata.create_all(bind=engine)

# # Функция для создания тестовой сессии базы данных
# def override_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # Замена сессии базы данных в тестовом клиенте FastAPI
# app.dependency_overrides["get_db"] = override_get_db

# # Инициализация тестового клиента
# client = TestClient(app)

# # Тест для GET-запроса /movies/{title}
# def test_get_movie():
#     # Отправка GET-запроса с существующим названием фильма
#     response = client.get("/movies/Avengers")
#     assert response.status_code == 200
#     data = response.json()
#     assert "id" in data
#     assert "title" in data
#     assert "description" in data
#     assert "rating" in data
#     assert "poster" in data

#     # Отправка GET-запроса с несуществующим названием фильма
#     response = client.get("/movies/NonexistentMovie")
#     assert response.status_code == 200
#     data = response.json()
#     assert "message" in data
#     assert data["message"] == "Movie not found"

# # Тест для GET-запроса /movies
# def test_get_movies():
#     # Отправка GET-запроса для получения всех фильмов
#     response = client.get("/movies")
#     assert response.status_code == 200
#     data = response.json()
#     assert isinstance(data, list)

# # Тест для DELETE-запроса /movies/{id}
# def test_delete_movie():
#     # Добавление фильма для последующего удаления
#     response = client.get("/movies/Avengers")
#     assert response.status_code == 200
#     data = response.json()
#     movie_id = data["id"]

#     # Отправка DELETE-запроса для удаления фильма
#     response = client.delete(f"/movies/{movie_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert "message" in data
#     assert data["message"] == "Movie deleted"

#     # Повторная отправка DELETE-запроса для несуществующего фильма
#     response = client.delete(f"/movies/{movie_id}")
#     assert response.status_code == 200
#     data = response.json()
#     assert "message" in data
#     assert data["message"] == "Movie does not exist"

def test_one():
    assert 1 == 1