def test_server_response(client):
    response = client.get('/')
    assert response.status_code == 200

def somar(a,b):
    return a+b


def test_somar():
    assert somar(2,2) == 4