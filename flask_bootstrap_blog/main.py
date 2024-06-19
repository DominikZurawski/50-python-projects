from flask import Flask, render_template, url_for, request
from post import Post
import smtplib
import os

OWN_EMAIL = os.environ["MY_EMAIL"]
OWN_PASSWORD = os.environ["MY_PASSWORD"]

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
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Successfully sent your message")

def send_email(name, email, phone, message):
    # Gmail: smtp.gmail.com | port 587
    # Hotmail: smtp.live.com
    # Outlook: outlook.office365.com
    # Yahoo: smtp.mail.yahoo.com
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}".encode('utf-8')
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
