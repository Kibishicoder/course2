from flask import Flask, render_template, request


from utils import get_posts_all, search_for_posts, get_posts_by_user, get_comments_by_post_id, get_post_by_pk

app = Flask(__name__)


@app.route("/")
def index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route("/posts/<int:uid>")
def post_page(uid):
    comment = get_comments_by_post_id(uid)
    posts = get_post_by_pk(uid)
    return render_template('post.html', comment=comment, posts=posts)


@app.route("/search/")
def search_page():
    search_by = request.args['s']
    if search_by:
        posts = search_for_posts(search_by)
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts)


@app.route("/users/<username>/")
def feed_page(username):
    user_feed = get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_feed)


if __name__ == "__main__":
    app.run(port=8000)
