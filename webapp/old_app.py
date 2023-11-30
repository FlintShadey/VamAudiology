from flask import Flask, jsonify, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "ec58e0a02e7d66b29d3c063d5a7293b8"



from flask import jsonify

@app.route("/", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if "login_submit" in request.form and login_form.validate_on_submit():
        # Login logic goes here...
        return jsonify(success=True)

    if "register_submit" in request.form and registration_form.validate_on_submit():
        # Registration logic goes here...
        return jsonify(success=True)

    return render_template(
        "login.html",
        title="Login",
        login_form=login_form,
        registration_form=registration_form,
    )

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Registration logic goes here...
        return jsonify(success=True, message="Your account has been created! You are now able to log in")
    else:
        # Return validation errors
        return jsonify(success=False, errors=form.errors), 400


@app.route("/landing_page")
def landing_page():
    # Check if 'registered' parameter is in the query string
    if 'registered' in request.args:
        flash("Your account has been created! You are now able to log in", "success")
    return render_template("landing-page.html", title="Home")



@app.route("/vam-audio-add")
def vam_audio_add():
    return render_template("vam-audio-add.html", title="Add Data")


@app.route("/vam-audio-download")
def vam_audio_download():
    return render_template("vam-audio-download.html", title="Download Data")


@app.route("/vam-audio-search")
def vam_audio_search():
    return render_template("vam-audio-search.html", title="Search Data")


if __name__ == "__main__":
    app.run(debug=True)
