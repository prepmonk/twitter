from .base import *
from backend.models.users_model import User

def test_create_user(client: TestClient):
    response = client.post("/users", json={'first_name': 'user', 'last_name': 'one', 'username': 'user1', 'password': '123'})
    data = response.json()
    print(data)
    assert response.status_code == 200  
    assert data["first_name"] == "user"  
    assert data["last_name"] == "one"  
    assert data["username"] == 'user1'
    assert data["id"] is not None


def test_all_users(client: TestClient, session: Session):
    user = User(first_name='test', last_name='1', username='user1', hashed_password='123')
    session.add(user)
    session.commit()

    response = client.get("/users")
    data = response.json()
    
    assert response.status_code == 200  
    assert len(data) == 1

def test_one_user(client: TestClient, session: Session):
    user1 = User(first_name='test', last_name='1', username='user1', hashed_password='123')
    user2 = User(first_name='test', last_name='2', username='user2', hashed_password='124')
    session.add(user1)
    session.add(user2)
    session.commit()

    response = client.get("/users/2")
    data = response.json()
    print(data)
    assert response.status_code == 200  
    
    assert data['first_name'] == 'test'
    assert data['last_name'] == '2'
    assert data['username'] == 'user2'
    assert data['id'] == 2

def test_followers(client: TestClient, session: Session):
    user1 = User(first_name='test', last_name='1', username='user1', hashed_password='123')
    user2 = User(first_name='test', last_name='2', username='user2', hashed_password='124')
    user3 = User(first_name='test', last_name='3', username='user3', hashed_password='125')
    user4 = User(first_name='test', last_name='4', username='user4', hashed_password='126')
    user5 = User(first_name='test', last_name='5', username='user5', hashed_password='127')
    
    session.add(user1)
    session.add(user2)
    session.add(user3)
    session.add(user4)
    session.add(user5)

    session.commit()

    response = client.post("/users/follow", json={'user_id': 1, 'follow_id': 2})
    data = response.json()
    assert response.status_code == 200

    response = client.post("/users/follow", json={'user_id': 1, 'follow_id': 3})
    data = response.json()
    assert response.status_code == 200

    response = client.post("/users/follow", json={'user_id': 2, 'follow_id': 1})
    data = response.json()
    assert response.status_code == 200

    response = client.post("/users/follow", json={'user_id': 2, 'follow_id': 3})
    data = response.json()
    assert response.status_code == 200

    response = client.post("/users/follow", json={'user_id': 2, 'follow_id': 4})
    data = response.json()
    assert response.status_code == 200

    response = client.post("/users/follow", json={'user_id': 4, 'follow_id': 1})
    data = response.json()
    assert response.status_code == 200


    response = client.get("/users/1")
    data = response.json()
    assert len(data['following']) == 2

    response = client.get("/users/2")
    data = response.json()
    assert len(data['following']) == 3

    response = client.get("/users/3")
    data = response.json()
    assert len(data['following']) == 0
    print(data)

    response = client.get("/users/4")
    data = response.json()
    assert len(data['following']) == 1
    