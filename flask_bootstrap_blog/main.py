from flask import Flask, render_template, url_for, request
from post import Post
import smtplib
import os

app = Flask(__name__)
posts = Post()


@app.route('/')
def home():
    posts_list = posts.all_post
    return render_template("index.html", list=posts_list)


@app.route('/post/<num>')
def post(num):
    blog_post = posts.get_post(int(num) - 1)
    return render_template("post.html", post=blog_post)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'GET':
        return render_template("contact.html")
    elif request.method == 'POST':
        data = request.form
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=RECEIVER_EMAIL,
                msg=f"Subject:Motivational Quote\n\n{random_quote["quote"]}\n \n{random_quote["author"]}")
        print(data["name"])
        print(data["email"])
        print(data["phone"])
        print(data["message"])
        return render_template("contact.html", message="Successfully sent your message")



if __name__ == "__main__":
    app.run(debug=True)
