from app import app

def test_soma():
    response = app.test_client().get('/soma?a=2&b=3')
    data = response.get_json()
    assert data['resultado'] == 5
