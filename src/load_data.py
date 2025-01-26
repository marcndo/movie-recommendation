import pandas as pd
ratings, movies = None, None

def load_data():
    """Load ratings and movies data set from csv files only once"""
    global ratings, movies
    if ratings is None or movies is None:
        ratings = pd.read_csv('data/rating.csv')
        movies = pd.read_csv('data/movie.csv')
    return ratings, movies
