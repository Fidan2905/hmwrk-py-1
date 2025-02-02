import requests


login = "fidanmahmudova2905@gmail.com"

# URL API
BASE_URL = "https://ru.yougile.com/api-v2"

# Тестовые данные
PROJECT_DATA = {
    "title": "Test Project"
}

INVALID_PROJECT_DATA = {
    "title": "",  # Поле обязательно
    "description": "This should fail due to missing name."
}

# Аутентификация (если требуется, добавьте ваш токен или необходимый заголовок)
HEADERS = {
    'Authorization': 'Bearer ZaTRqRUoW8oCnHHY4NJm+LSzQw79ii68fS9N2pn9e0Y49Oc54WRHtQn4nIJrM0Ej', # Раскомментируйте и добавьте ваш токен
    'Content-Type': 'application/json'
}


# Позитивные тесты
def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_specific_project():
    project_id = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS).json()["id"]
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == project_id


def test_update_project():
    project_id = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS).json()["id"]
    update_data = {
        "title": "Updated Project"
    }

    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200  #


def test_get_projects():
    response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
    assert response.status_code == 200


    # Негативный тест
def test_create_project_missing_name():
    response = requests.post(f"{BASE_URL}/projects", json=INVALID_PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 400