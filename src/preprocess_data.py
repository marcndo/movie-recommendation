import pandas as pd
from scipy.sparse import csr_matrix


def preprocess_data(ratings):
    """Handle missing values and create user-item matrix"""
    ratings = ratings.dropna()
    user_movies_matrix = ratings.pivot(index='userId', columns='movieId', values='rating').fillna(0)
    return user_movies_matrix