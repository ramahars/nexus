def test_create_dataset(client):
    response = client.post(
        "/datasets/",
        json={
            "name": "Test dataset",
            "description": "A dataset created during testing.",
        },
    )

    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Test dataset"
    assert data["description"] == "A dataset created during testing."
    assert "id" in data
    assert "created_at" in data


def test_list_datasets(client):
    client.post(
        "/datasets/",
        json={"name": "Dataset 1"},
    )

    response = client.get("/datasets/")

    assert response.status_code == 200

    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Dataset 1"


def test_create_dataset_validation_error(client):
    response = client.post(
        "/datasets/",
        json={"description": "Missing name"},
    )

    assert response.status_code == 422
