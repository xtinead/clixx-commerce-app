from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_liveness():
    response = client.get("/health/live")

    assert response.status_code == 200
    assert response.json() == {"status": "alive"}


def test_list_products():
    response = client.get("/products")

    assert response.status_code == 200

    products = response.json()

    assert len(products) == 3
    assert products[0]["name"] == "Running Shoes"


def test_get_existing_product():
    response = client.get("/products/1")

    assert response.status_code == 200
    assert response.json()["id"] == 1
    assert response.json()["price"] == 89.99


def test_get_missing_product():
    response = client.get("/products/999")

    assert response.status_code == 404
    assert response.json() == {
        "detail": "Product not found"
    }


def test_invalid_product_id():
    response = client.get("/products/invalid")

    assert response.status_code == 422
