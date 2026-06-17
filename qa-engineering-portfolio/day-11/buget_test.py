import requests
import pytest
import uuid

BASE_URL = "http://localhost:8080/api/v1"


@pytest.fixture
def register_user():
    import uuid

    username = f"user_{uuid.uuid4().hex[:8]}"
    payload = {
        "email": username + "@gmail.com",
        "firstName": "Fathia",
        "lastName": "Oyinloye",
        "password": "fathiaoyinloye21",
        "username": username
    }

    response = requests.post(
        f"{BASE_URL}/auth/new_user",
        json=payload
    )

    response_body = response.json()
    assert "token" in response_body

    token = response_body["token"]
    assert token != ""
    assert token.count(".") == 2
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    return headers



def test_budget_cannot_be_created_with_unauthenticated_user():
    payload = {
        "name": "",
        "period": "MONTHLY"
    }

    response = requests.post(
        f"{BASE_URL}/budget",
        json=payload,
    )

    assert response.status_code == 401


def test_user_create_budget_with_valid_data(register_user):
    payload = {
        "name": "Monarch Payment",
        "period": "MONTHLY"
    }

    response = requests.post(
        f"{BASE_URL}/budget",
        json=payload,
        headers=register_user
    )

    assert response.status_code == 201

def test_budget_name_cannot_be_empty(register_user):
    payload = {
        "name": "",
        "period": "MONTHLY"
    }

    response = requests.post(
        f"{BASE_URL}/budget",
        json=payload,
        headers=register_user
    )

    assert response.status_code == 400


@pytest.mark.parametrize(

    "invalid_name",

    [

        "",

        " ",

        123,

        True

    ]

)
def test_budget_name_validation(register_user, invalid_name):
        payload = {

            "name": invalid_name,

            "period": "MONTHLY"

        }

        response = requests.post(

            f"{BASE_URL}/budget",

            json=payload,

            headers=register_user

        )

        assert response.status_code == 400




