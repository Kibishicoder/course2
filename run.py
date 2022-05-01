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
    return render_template('post.html', comment=comment)


@app.route("/search/?s=")
def search_page():
    search_by = request.args['s']
    if search_by:
        posts = get_posts_by_user(search_by)
        if posts:
            return render_template('search.html', search_by=search_by, posts=posts)


@app.route("/feed/users/<username>")
def feed_page():
    user_feed = get_post_by_pk()
    return render_template('user-feed.html', )


# @app.route("/tag/")
# def tag_page():
#     search_by_tag = request.args['s']
#     if search_by_tag:
#         posts = search_for_posts(search_by_tag)
#         if posts:
#             return render_template('tag.html', search_by_tag=search_by_tag, posts=posts)





if __name__ == "__main__":
    app.run(port=8000)
