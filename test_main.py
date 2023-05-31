from fastapi.testclient import TestClient
from main import app

# Инициализация тестового клиента
client = TestClient(app)

# Тест для GET-запроса /movies/{title}
def test_get_movie():
    # Отправка GET-запроса с существующим названием фильма
    response = client.get("/movies/Avengers")
    assert response.status_code == 200
    if type(response.json()) == dict:
        if response.json()["message"] == "Movie already exists":
            return
    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "description" in data
    assert "rating" in data
    assert "poster" in data

    # Отправка GET-запроса с несуществующим названием фильма
    response = client.get("/movies/NonexistentMovie")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Movie not found"

# Тест для GET-запроса /movies
def test_get_movies():
    # Отправка GET-запроса для получения всех фильмов
    response = client.get("/movies")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Тест для DELETE-запроса /movies/{id}
def test_delete_movie():
    # Добавление фильма для последующего удаления
    response = client.get("/movies/She")
    assert response.status_code == 200
    data = response.json()
    if type(response.json()) == dict:
        if response.json()["message"] == "Movie already exists":
            return
        return
    movie_id = data["id"]


    # Отправка DELETE-запроса для удаления фильма
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Movie deleted"

    # Повторная отправка DELETE-запроса для несуществующего фильма
    response = client.delete(f"/movies/{movie_id}")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "Movie does not exist"

def test_one():
    assert 1 == 1