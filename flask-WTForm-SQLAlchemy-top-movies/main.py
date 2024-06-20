from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

TMDB_API = os.environ["API"]
MOVIE_DB_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
MOVIE_DB_SEARCH_URL = "https://api.themoviedb.org/3/search/movie"
MOVIE_DB_INFO_URL = "https://api.themoviedb.org/3/movie"


class EditForm(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g. 7.5')
    review = StringField('Your Review')
    submit = SubmitField(label="Done")

class AddMovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField(label="Add Movie")

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# CREATE DB
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

def query_movie(title):
    config = {
        "query": title,
        "include_adult": "false",
        "language": "pl-PL",
        "page": "1",
    }
    headers = {
        "accept": "application/json",
        "Authorization": TMDB_API,
    }
    response = requests.get(url=MOVIE_DB_SEARCH_URL, params=config, headers=headers)
    data = response.json()["results"]
    return data

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=True)
    ranking: Mapped[int] = mapped_column(Integer, nullable=True)
    review: Mapped[str] = mapped_column(String(250), nullable=True)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)


# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

    # CREATE RECORDS
    new_movie = Movie(
        title="Phone Booth",
        year=2002,
        description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
        rating=7.3,
        ranking=10,
        review="My favourite character was the caller.",
        img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
    )

    second_movie = Movie(
        title="Avatar The Way of Water",
        year=2022,
        description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
        rating=7.3,
        ranking=8,
        review="I liked the water.",
        img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
    )
    #
    # db.session.add(new_movie)
    # db.session.commit()
    # db.session.add(second_movie)
    # db.session.commit()

@app.route("/")
def home():
    # READ ALL RECORDS
    # Construct a query to select from the database. Returns the rows in the database
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    # Use .scalars() to get the elements rather than entire rows from the database
    all_movies = result.scalars().all()

    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()

    return render_template("index.html", movies=all_movies)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        data = query_movie(form.title.data)
        return render_template("select.html", options=data)
    return render_template("add.html", form=form)


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = EditForm()
    movie_id = request.args.get('id')
    movie_selected = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        # UPDATE RECORD
        movie_selected.rating = float(request.form["rating"]) # or: float(form.rating.data) #
        movie_selected.review = request.form["review"]
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("edit.html", form=form, movie=movie_selected)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')

    # DELETE A RECORD BY ID
    movie_to_delete = db.get_or_404(Movie, movie_id)
    # Alternative way to select the book to delete.
    # book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
        headers = {
            "accept": "application/json",
            "Authorization": TMDB_API,
        }
        response = requests.get(movie_api_url, params={"language": "pl-PL"}, headers=headers)
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            #The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
