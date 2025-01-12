import pandas as pd


def load_data():
    """Load ratings and movies data set from csv files"""
    ratings = pd.read_csv('data/rating.csv')
    movies = pd.read_csv('data/movie.csv')
    return ratings, movies

def explore_data(ratings, movies):
    """Explore the data to check for missing values and 
    descriptive statistics"""
    print(ratings.head())
    print(movies.head())
    print(ratings.isnull().sum())
    print(movies.isnull().sum())
    print(ratings['rating'].describe())
    ratings['rating'].value_counts().sort_index().plot(kind='bar')

