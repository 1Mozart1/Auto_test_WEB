import pytest
import requests
import yaml

from check_post import get_login

with open('config.yaml') as file:
    data = yaml.safe_load(file)


@pytest.fixture()
def token():
    return get_login()


@pytest.fixture()
def create_post():
    post = requests.post(url=data.get('url_post'), headers={"X-Auth-Token": data['token']}, data={
        'username': 'Neo1',
        'password': '9aedda8a1f',
        'title': 'Dog',
        'description': 'about dog',
        'content': 'Плацентарное млекопитающее отряда хищных семейства псовых.'})
    return post.json()['description']
