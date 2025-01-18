from src.evaluate_model import evaluate_model
from src.preprocess_data import preprocess_data
from src.load_data import load_data, explore_data
from src.collaborative_filtering import collaborative_filtering



def get_recommendation(user_id, algo, movies, ratings):
    """Generate movie recommendation for a specific user."""

    user_movies = ratings[ratings['userId'] == user_id]['movieId'].tolist()
    all_movies = movies['movieId'].tolist()
    unrated_movies = [movie for movie in all_movies if movie not in user_movies]

    #Predict ratings 
    recommender = []
    for movie_id in unrated_movies:
        prediction = algo.predict(user_id, movie_id)
        recommender.append([movie_id, prediction.est])
        recommendations = sorted(recommendations, key=lambda x: x[1], reverse=True)[:10]
        recommended_titles = [movies[movies['movieId'] == movie[0]]['title'].values[0] for movie in recommendations]
    return recommended_titles


def main():
    #Load and explore the data
    ratings, movies = load_data()
    explore_data(ratings, movies)

    #Preprocess data
    user_movie_matrix = preprocess_data(ratings)

    #Build collaborative filter model
    algo = collaborative_filtering(ratings)
    
    user_id = 1  # Replace with a real user ID from your dataset

    recommendations = get_recommendation(user_id, algo, movies, ratings)
    print(f"Recommendations for User {user_id}: {recommendations}")
    
    #Evaluate the model
    rmse = algo.test(algo.trainset.build_testset())
    evaluate_model(rmse)

if __name__ == '__main__':
    main()