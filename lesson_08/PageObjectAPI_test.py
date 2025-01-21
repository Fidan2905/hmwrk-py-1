import requests
import pytest


BASE_URL = "https://ru.yougile.com/api-v2"

PROJECT_DATA = {
    "name": "Test Project",
    "description": "This is a test project."
}

INVALID_PROJECT_DATA = {
    "name": "",
    "description": "This should fail due to missing name."
}

HEADERS = {
    'Content-Type': 'application/json'
}


# Позитивные тесты
def test_create_project():
    response = requests.post(f"{BASE_URL}/projects", json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 201
    assert "id" in response.json()

def test_get_specific_project():
    project_id = 1  # Необходимо заменить на актуальный ID проекта для получения точных тестовых данных
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['id'] == project_id


def test_update_project():
    project_id = 1  # Необходимо заменить на актуальный ID проекта для получения точных тестовых данных
    update_data = {
        "name": "Updated Project",
        "description": "This project has been updated."
    }

    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200 
    assert response.json()['name'] == "Updated Project"


    def test_get_projects():
        response = requests.get(f"{BASE_URL}/projects", headers=HEADERS)
        assert response.status_code == 200
        assert isinstance(response.json(), list)


    # Негативный тест
def test_create_project_missing_name():
    response = requests.post(f"{BASE_URL}/projects", json=INVALID_PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 400
    assert "name" in response.json()['errors']

if __name__ == "__main__":
    pytest.main()
