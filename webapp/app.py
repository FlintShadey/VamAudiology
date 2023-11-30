from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "ec58e0a02e7d66b29d3c063d5a7293b8"

@app.route("/", methods=["GET", "POST"])
def home():
    login_form = LoginForm()
    registration_form = RegistrationForm()

    if request.method == "POST":
        if "login_submit" in request.form and login_form.validate_on_submit():
            # Placeholder for future login validation logic
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

if __name__ == "__main__":
    app.run(debug=True)
