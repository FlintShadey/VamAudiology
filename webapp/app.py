from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ec58e0a02e7d66b29d3c063d5a7293b8"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"

db = SQLAlchemy(app)
'''
to initialize the database, open a python shell in the terminal and type:
from app import db
db.create_all()

but i  had to do this:
from app import app, db
with app.app_context():
    db.create_all()

'''

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),unique=True, nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"
    
class audiology_data(db.Model):
    data_id = db.Column(db.Integer, primary_key=True)
    last_name = db.Column(db.String(20), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    date_of_test = db.Column(db.String(20), nullable=False)
    side = db.Column(db.String(20), nullable=False)
    freq_500  = db.Column(db.Integer, nullable=False)
    freq_1K = db.Column(db.Integer, nullable=False)
    freq_2K = db.Column(db.Integer, nullable=False)
    freq_3K = db.Column(db.Integer, nullable=False)
    freq_4K = db.Column(db.Integer, nullable=False)
    freq_6K = db.Column(db.Integer, nullable=False)
    freq_8K = db.Column(db.Integer, nullable=False)



@app.route("/", methods=["GET", "POST"])
def home():
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == "POST":
        if "login_submit" in request.form and login_form.validate_on_submit():
            # Placeholder for future login validation logic
                # if form.validate_on_submit():
                #     if form.email.data == "admin@blog.com" and form.password.data == "password":
                #         flash("You have been logged in!", "success")
                #         return redirect(url_for("home"))
                #     else:
                #         flash("Login Unsuccessful. Please check username and password", "danger")
            flash("Logged in successfully!", "success")
            return redirect(url_for('landing_page'))

        if "register_submit" in request.form and registration_form.validate_on_submit():
            # Placeholder for future registration logic
            flash("Registered successfully!", "success")
            return redirect(url_for('landing_page'))

    return render_template("login.html", login_form=login_form, registration_form=registration_form)

@app.route("/landing_page")
def landing_page():
    return render_template("landing-page.html", title="Home")

@app.route("/vam-audio-add")
def vam_audio_add():
    return render_template("vam-audio-add.html")

@app.route("/vam-audio-download")
def vam_audio_download():
    return render_template("vam-audio-download.html")

@app.route("/vam-audio-search")
def vam_audio_search():
    return render_template("vam-audio-search.html")

if __name__ == "__main__":
    app.run(debug=True)
