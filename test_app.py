from app import app
def test_app_root_url():
    with app.test_client() as c:
        response = c.get('/')
        assert response.data == b'Hello Everyone!'
        assert response.status_code == 200
