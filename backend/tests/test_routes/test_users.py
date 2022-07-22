import json


def test_create_user(client):
	data = {
		"username": "testuser",
		"email": "testuser@server.de",
		"password": "testing",
	}
	response = client.post("/users/", json.dumps(data))
	assert response.status_code == 200
	assert response.json()["email"] == "testuser@server.de"
	assert response.json()["is_active"] == True
