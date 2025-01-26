import numpy as np
from surprise import Reader, Dataset, SVD
from surprise.model_selection import train_test_split
from surprise.model_selection import cross_validate

algo = None
def collaborative_filtering(ratings):
    """Build and evaluate a collaborative filtering"""
    global algo
    if algo is None:
        reader = Reader(rating_scale=(1,5))
        data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
        np.random.seed(42)
        trainset,_ = train_test_split(data, test_size=0.2)
        algo = SVD()
        algo.fit(trainset)
        print('Model trained successfully!')
    return algo