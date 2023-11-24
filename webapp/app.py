from flask import Flask, render_template, redirect, url_for, flash, request
from forms import LoginForm, RegistrationForm


app = Flask(__name__)

app.config["SECRET_KEY"] = "ec58e0a02e7d66b29d3c063d5a7293b8"



# @app.route('/', methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         # Insert logic to verify the user's login credentials here
#         flash('You have been logged in!', 'success')
#         # Redirect to the dashboard or another page on successful login
#         return redirect(url_for('/landing-page'))
#     return render_template('login.html', title='Login', form=form)

@app.route('/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    registration_form = RegistrationForm()  # Add this line to create an instance of RegistrationForm
    if form.validate_on_submit():
        # Login logic goes here...
        flash('You have been logged in!', 'success')
        return redirect(url_for('landing_page'))  # Make sure this is the function name, not the endpoint
    return render_template('login.html', title='Login', form=form, registration_form=registration_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        # Insert logic to register the user here
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))  # Redirect back to the login page
    # Pass the registration form as a separate variable
    return render_template('login.html', title='Register', registration_form=form, form=LoginForm())



@app.route('/landing-page')
def landing_page(): 
    return render_template('landing-page.html',  title='Home')

@app.route('/vam-audio-add')
def vam_audio_add():
    return render_template('vam-audio-add.html', title='Add Data')

@app.route('/vam-audio-download')
def vam_audio_download():
    return render_template('vam-audio-download.html', title='Download Data')

@app.route('/vam-audio-search')
def vam_audio_search():
    return render_template('vam-audio-search.html', title='Search Data')

if __name__ == '__main__':
    app.run(debug=True)
