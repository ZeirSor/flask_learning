import requests

import sys


def test1():
    res_get = requests.get('http://127.0.0.1:5002/hello')
    res_post = requests.post('http://127.0.0.1:5002/hello')
    res_put = requests.put('http://127.0.0.1:5002/hello')
    res_delete = requests.delete('http://127.0.0.1:5002/hello')
    print(res_get.json())
    print(res_post.json())
    print(res_put.json())
    print(res_delete.json())

    # print(res_get.text)
    # print(res_post.text)
    # print(res_put.text)
    # print(res_delete.text)


# test()

def test2():
    res_get = requests.get('http://127.0.0.1:5002/user')
    res_post = requests.post('http://127.0.0.1:5002/user')
    res_put = requests.put('http://127.0.0.1:5002/user')
    res_delete = requests.delete('http://127.0.0.1:5002/user')
    print(res_get.text)
    print(res_post.text)
    print(res_put.text)
    print(res_delete.text)


# test2()

def test3():
    res_get = requests.get('http://127.0.0.1:5002/user2',
                           # json={'name': 'lisi'},
                           headers={'Content-Type': 'application/json'},
                           )

    print(res_get.json())


# test3()

def test_json(route: str):
    res_get = requests.get('http://127.0.0.1:5002/' + route,
                           json={
                               'name': 'lisi',
                               'age': [33, 44],
                           },
                           headers={'Content-Type': 'application/json',
                                    'Cookie': 'key=1dms85oKayA1WqW5x.zG1pzHyl2qoc_.zI82TVTXWcw-1697634932-0-Abk21TEH2L8YXL5f8MLivvNJt5NLv0j9mw/AI83VH50+npc9SeNCDWUhBt31fPMhav0IcUHbOOaY36y7FsYxHFA='},
                           )
    print(res_get.json())


if __name__ == '__main__':
    args = sys.argv
    # print(args)
    # print(args)
    test_json(args[1])
