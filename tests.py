import pytest

from run import app


def test_list():





def test_keys():
    response = app.test_client().get('/api/posts/')
    keys_needed = ['content', 'poster_name', 'poster_avatar', 'pic', 'views_count', 'likes_count', 'pk']
    for el in response.json:
        for key in keys_needed:
            assert (bool(key in el.keys()) == True), key in el.keys()
            assert keys_needed and el.keys() == keys_needed

    response = app.test_client().get('/api/posts/')
    assert response.status_code == 200
    assert response.data == b'it works'
