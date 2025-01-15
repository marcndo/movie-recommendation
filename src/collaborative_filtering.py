from surprise import Reader, Dataset, SVD, KNNBasic
from surprise.model_selection import train_test_split
from surprise import accuracy
from scipy.sparse import csr_matrix

def collaborative_filtering(ratings):
    """Build and evaluate a collaborative filtering"""
    reader = Reader(rating_scale=(1,5))
    data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
    
    #split dataset into train test splits
    trainset, testset = train_test_split(data, test_size=0.2)

    # Initialize the collaborative filtering algorithm (user-based)
    #algo = KNNBasic(sim_options={'name': 'cosine', 'user_based': True})
    algo = SVD()
    algo.fit(trainset)

    # Make predictions on the test set
    predictions = algo.test(testset)
    
    # Calculate and return RMSE
    rmse = accuracy.rmse(predictions)
    return rmse