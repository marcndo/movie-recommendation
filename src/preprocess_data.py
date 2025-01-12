import pandas as pd

def preprocess_data(ratings):
    """Handle missing values and create user-item matrix"""
    ratings = ratings.dropna()
    user_movies_matrix = ratings.pivot(index='userId', columns='movieId', values='rating')
    return user_movies_matrix