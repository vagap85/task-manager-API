def test_create_task(client):
    response = client.post(
        "/tasks/",
        json={"title": "Test Task", "status": "pending"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert "id" in data


def test_get_tasks(client):
    client.post("/tasks/", json={"title": "Test"})
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_task_api_full_flow(client):
    # 1. Создание
    create_resp = client.post("/tasks/", json={"title": "Flow Test", "status": "pending"})
    assert create_resp.status_code == 200
    task_id = create_resp.json()["id"]

    # 2. Получение по ID
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["title"] == "Flow Test"

    # 3. Обновление
    update_resp = client.put(f"/tasks/{task_id}", json={"title": "Updated Title"})
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == "Updated Title"

    # 4. Удаление
    delete_resp = client.delete(f"/tasks/{task_id}")
    assert delete_resp.status_code == 200

    # 5. Проверка что удалено
    get_after_delete = client.get(f"/tasks/{task_id}")
    assert get_after_delete.status_code == 404