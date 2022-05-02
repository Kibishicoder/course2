import json

POST_PATH = "data/data.json"
COMMENT_PATH = "data/comments.json"


def get_posts_all():
    """возвращает посты"""

    with open(POST_PATH, 'r', encoding='utf8') as file:
        posts = json.load(file)
        return posts


def get_comments_by_post_id(post_id):
    """возвращает комментарии определенного поста"""
    with open(COMMENT_PATH, "r", encoding="utf-8") as file:
        comments = json.load(file)
        comments_by_id = []
        for comment in comments:
            if post_id == comment['post_id']:
                comments_by_id.append(comment)
    return comments_by_id


def get_posts_by_user(user_name):
    """возвращает посты определенного пользователя"""
    with open(POST_PATH, 'r', encoding='utf8') as file:
        user_data = json.load(file)
    return [posts for posts in user_data if user_name in posts['poster_name'].lower()]


def search_for_posts(search_by_tag):
    """возвращает список постов по ключевому слову"""
    post_list = get_posts_all()
    posts_list = []

    for post in post_list:
        if search_by_tag.lower() in post['content'].lower():
            posts_list.append(post)
    return posts_list


def get_post_by_pk(pk):
    """возвращает один пост по его идентификатору"""
    user_data = get_posts_all()
    for poster in user_data:
        if poster['pk'] == pk:
            return {
                'poster_name': poster['poster_name'],
                'content': poster['content'],
                'poster_avatar': poster['poster_avatar']
            }


# Напишите к каждой функции юнит тесты, расположите тесты в отдельной папке `/tests`.
#
# Организуйте тесты в виде классов или функций, на ваше усмотрение.
