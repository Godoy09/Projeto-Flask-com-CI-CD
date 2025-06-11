from app import app

def test_tipo_resposta():
    response = app.test_client().get('/soma?a=1&b=2')
    data = response.get_json()
    assert isinstance(data['resultado'], int)
