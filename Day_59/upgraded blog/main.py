from flask import Flask, render_template, request
import requests
import smtplib

app = Flask(__name__)

all_posts = requests.get('https://api.npoint.io/dbecbee1d9f5685aaa7b').json()


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=all_posts)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        send_email(name=request.form['username'], email=request.form['email'], phone=request.form['phone'],
                   message=request.form['message'])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_email(name, email, phone, message):
    email_massage = f"Subject:New Message from Blog\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user='my_email', password='123456')
        connection.sendmail(from_addr='my_email',
                            to_addrs='another_email',
                            msg=email_massage)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in all_posts:
        if blog_post['id'] == index:
            requested_post = blog_post
    return render_template('post.html', post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
