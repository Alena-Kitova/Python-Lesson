import pytest
from projects_yougile import ProjectYouGile


BASE_URL = "https://ru.yougile.com"
TOKEN = "1tZZYfp9hH+l8UDsZwXe4oPh9s16l1YCGzErT4yCdfyQ01EP6wEwEAnDKABnfanM"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {TOKEN}"
}


@pytest.fixture(scope="module")
def project_page():
    return ProjectYouGile(BASE_URL, TOKEN)


@pytest.fixture(scope="module")
def create_project(project_page):
    response = project_page.create_project("Курс 106.2")
    assert response.status_code == 201
    project_id = response.json()["id"]
    return project_id


# POST /api-v2/projects
def test_create_project_positive(project_page):
    response = project_page.create_project("Проект")
    assert response.status_code == 201
    new_id = response.json()["id"]
    return new_id


def test_create_project_negative_no_title(project_page):
    response = project_page.create_project(title=None)
    assert response.status_code == 400


# GET /api-v2/projects/{id}
def test_get_project_positive(project_page, create_project):
    new_id = create_project
    response = project_page.get_project(new_id)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == new_id
    assert "title" in data


def test_get_project_negative_not_found(project_page):
    invalid_id = "123"
    response = project_page.get_project(invalid_id)
    assert response.status_code == 404


# PUT /api-v2/projects/{id}
def test_update_project_positive(project_page, create_project):
    new_id = create_project
    response = project_page.update_project(new_id, "Новый проект")
    assert response.status_code == 200
    updated_id = response.json()["id"]
    return updated_id


def test_update_project_negative_invalid_id(project_page):
    invalid_id = "123"
    response = project_page.update_project(invalid_id, "Обновленный проект")
    assert response.status_code == 404
