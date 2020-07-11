from pytest_practice.app import mysum, get_user_data
import requests
import pytest

@pytest.mark.parametrize("a,b", [
    (2,3),
    (10, 9),
    (5, 12)
])
def test_sum(a, b):
    assert mysum(a,b) == 5

def test_get_user_data():
    user_data = get_user_data("Naresh")
    assert user_data.get("age") == 24

def test_dummy_api():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    data = response.json()
    assert len(data) == 100
