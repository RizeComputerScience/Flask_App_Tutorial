from flask import Blueprint, render_template

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route("/movies")
def movie_list():
    movies = [
        {"title": "The Shawshank Redemption", "year": 1994},
        {"title": "Inception", "year": 2010},
        {"title": "Everything Everywhere All At Once", "year": 2022},
    ]
    return "Welcome to the movies page. We want our movies to be shown here!"