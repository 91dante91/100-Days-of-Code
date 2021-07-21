from flask import Flask, render_template
import requests
from post import Post


app = Flask(__name__)

all_posts = requests.get('https://api.npoint.io/ed99320662742443cc5b').json()
post_objects = []
for post in all_posts:
    post_object = Post(post_id=post['id'], title=post['title'], subtitle=post['subtitle'], body=post['body'])
    post_objects.append(post_object)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_objects)

@app.route('/posts/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
