from app import app

def test_home():
    response = app.test_client().get("/")
    assert response.status_code == 200

def test_add():
    response = app.test_client().get("/add/10/20")
    assert response.status_code == 200