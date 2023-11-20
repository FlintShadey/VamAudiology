from flask import Flask, render_template, url_for, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title='Login')

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
