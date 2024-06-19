from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, URLField, TimeField
from wtforms.validators import DataRequired, URL, InputRequired
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


class CafeForm(FlaskForm):
    coffee_list = ['✘', '☕️', '☕️☕️', '☕️☕️☕️', '☕️☕️☕️☕️', '☕️☕️☕️☕️☕️']
    power_list = ['✘', '🔌', '🔌🔌','🔌🔌🔌', '🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌']
    wifi_list = ['✘', '💪', '💪💪',  '💪💪💪', '💪💪💪💪️', '💪💪💪💪💪']
    cafe = StringField('Cafe name', validators=[InputRequired()])
    location = URLField('Cafe Location on Google Maps (URL)', validators=[InputRequired(), URL()])
    opening_time = TimeField('Opening Time e.g. 8AM', validators=[DataRequired()])
    closing_time = TimeField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    c_rating = SelectField('Coffee Rating', choices={"rate": coffee_list}, validators=[DataRequired()])
    wifi = SelectField('Wifi Strength Rating', choices={"mark": wifi_list}, validators=[DataRequired()])
    power = SelectField('Power Socket Availability', choices={"mark": power_list}, validators=[DataRequired()])
    submit = SubmitField('Submit')


# Exercise:

# make all fields required except submit
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open("cafe-data.csv", 'a', encoding='utf-8') as file:
            file.write(
                f"\n{form.cafe.data},{form.location.data},{form.opening_time.data.strftime('%I:%M%p')}.{form.closing_time.data.strftime('%I:%M%p')},{form.c_rating.data},{form.wifi.data},{form.power.data}")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True, port=5002)
