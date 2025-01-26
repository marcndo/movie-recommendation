from src.load_data import load_data
from src.collaborative_filtering import collaborative_filtering


recommendation_cache = {}
def get_recommendation(user_id, algo, movies, ratings):
    try:
        if user_id in recommendation_cache:
            return recommendation_cache[user_id]
    
        # Get all unique movie IDs
        all_movie_ids = movies['movieId'].unique()
        
        # Predict ratings for all movies not yet rated by the user
        watched_movie_ids = ratings[ratings['userId'] == user_id]['movieId'].unique()
        unwatched_movie_ids = [movie_id for movie_id in all_movie_ids if movie_id not in watched_movie_ids]

        # Batch predict ratings for unwatched movies
        predictions = [algo.predict(user_id, movie_id) for movie_id in unwatched_movie_ids]
        # Sort recommendations by estimated rating
        recommendations = sorted(predictions, key=lambda x: x.est, reverse=True)[:10]
        # Get movie titles
        #recommended_movies = [movies.loc[movies['movieId'] == movie_id, 'title'].values[0] for movie_id, _ in recommendations]
        recommended_movies = [movies.loc[movies['movieId'] == pred.iid, 'title'].values[0] for pred in recommendations]
        recommendation_cache[user_id] = recommended_movies
        return recommended_movies
    except Exception as e:
        print(f"Error in get_recommendation: {e}")
        raise []
