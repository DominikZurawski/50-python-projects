# Documentation: https://jinja.palletsprojects.com/en/2.11.x/templates/
from flask import Flask, render_template
import random
from datetime import datetime
import requests
from post import Post

app = Flask(__name__)
posts = Post()

@app.route('/')
def home():
    posts_list = posts.all_post
    return render_template("index.html", list=posts_list)


@app.route('/post/<num>')
def post(num):
    blog_post = posts.get_post(int(num)-1)
    return render_template("post.html", post=blog_post)


@app.route('/home')
def home2():
    year = datetime.now().strftime("%Y")
    random_number = random.randint(1, 10)
    return render_template("index1.html", num=random_number, year=year)


@app.route("/guess/<name>")
def guess(name):
    param = {
        'name': name,
    }
    age_url = "https://api.agify.io"
    response = requests.get(url=age_url, params=param)
    response.raise_for_status()
    age_response = response.json()

    gender_url = "https://api.genderize.io"
    response_gender = requests.get(url=gender_url, params=param)
    response_gender.raise_for_status()
    gender_response = response_gender.json()

    year = datetime.now().strftime("%Y")

    return render_template("guess.html", name=name, age=age_response['age'], gender=gender_response['gender'],
                           year=year)


@app.route("/blog/<num>")
def blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_post = response.json()
    return render_template("blog.html", posts=all_post)


if __name__ == "__main__":
    app.run(debug=True)
