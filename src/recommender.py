from load_data import load_data, explore_data
from preprocess_data import preprocess_data
from collaborative_filtering import collaborative_filtering
from evaluate_model import evaluate_model


def get_recommendation(user_id, algo, movies, ratings):
    """Generate movie recommendation for a specific user."""

    user_movies = ratings[ratings['user_id'] == user_id['movieId']].tolist()
    all_movies = movies['movieId'].tolist()
    unrated_movies = [movie for movie in all_movies if movie not in user_movies]

    #Predict ratings 
    recommender = []
    for movie_id in unrated_movies:
        prediction = algo.predict(user_id, movie_id)
        recommender.append(movie_id, prediction.est)
        recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:10]
        recommended_titles = [movies[movies['movieId'] == movie[0]]['title'].values[0] for movie in recommendations]
    return recommended_titles


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