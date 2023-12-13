import requests
import yaml

with open('config.yaml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)


def get_login():
    path = data['url_login']
    post = requests.post(url=path, data={'username': data['username'], 'password': data['password']})
    if post.status_code == 200:
        return post.json()['token']


def get_post(token):
    path = data['url_post']
    get = requests.get(url=path, data={'username': data['username'], 'password': data['password']},
                       headers={"X-Auth-Token": token})
    if get.status_code == 200:
        return get.json()


if __name__ == '__main__':
    token = get_login()
    print(get_post(token))
