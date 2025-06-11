from app import app

def test_status_code():
    response = app.test_client().get('/soma?a=1&b=2')
    assert response.status_code == 200
