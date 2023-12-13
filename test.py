import yaml

from check_post import get_post

with open('config.yaml') as file:
    data = yaml.safe_load(file)

# id_check = 92332
id_check = 92333


def test_1(token):
    output = get_post(token)['data']
    res = []
    for item in output:
        res.append(item['id'])
    assert id_check in res


def test_create_post(create_post):
    assert 'about dog' in create_post
