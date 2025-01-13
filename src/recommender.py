from load_data import load_data, explore_data
from preprocess_data import preprocess_data
from collaborative_filtering import collaborative_filtering
from evaluate_model import evaluate_model

def main():
    #Load and explore the data
    ratings, movies = load_data()
    explore_data(ratings, movies)

    #Preprocess data
    user-movie-matrix = preprocess_data(ratings)

    #Build collaborative filter model
    rmse = collaborative_filtering(ratings)
    
    #Evaluate the model
    evaluate_model(rmse)

if __name__ == '__main__':
    main()