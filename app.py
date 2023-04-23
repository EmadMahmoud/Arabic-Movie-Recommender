from flask import Flask, render_template, request, redirect, url_for
from model import model_func


app = Flask(__name__)


@app.route('/')
def landing_page():
    return render_template('landing.html')


@app.route('/submit-form', methods=['POST'])
def handle_form_submission():
    form_data = request.form
    movie_name = form_data.get('name')
    reco_movies = model_func(movie_name)
    if len(reco_movies) < 1:
        reco_movies = [" أدخل اسم فيلم صحيح باللغه العربيه"]
    return render_template('sugmovies.html',  movies=reco_movies)


@app.route('/entername')
def form_page():  # put application's code here
    return render_template('index.html')













