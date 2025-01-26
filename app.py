from flask import Flask, request, jsonify
from src.recommender import collaborative_filtering, load_data, get_recommendation

app = Flask(__name__)

# Global variable to store the model
ratings = None
movies = None
model = None

@app.before_request
def initialize_model():
    global ratings, movies, model
    ratings, movies = load_data()  # Load data once
    model = collaborative_filtering(ratings)

@app.route("/")
def home():
    return "Welcome to the movie recommendation app!😊"

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('userId', type=int)
    if not user_id:
        return jsonify({'error': 'user id is required'}), 400

    try:
        if not model:
            return jsonify({"error": "Model not initialized"}), 500
        print(f"User ID: {user_id}")
        print(f"Model: {model}")
        print(f"Movies: {movies.head()}")
        print(f"Ratings: {ratings.head()}")
        recommendation = get_recommendation(user_id,model,movies,ratings)

        if not recommendation:
            return jsonify({'error': 'No recommendation found for this user. This could be due to insufficient data or ratings.'}), 404
        
        return jsonify({"recommendation": recommendation})
    
    except Exception as e:
        print(f"Error during recommendation: {e}")
        return jsonify({"error":"An error occurred during recommendation process"}), 500


if __name__ == '__main__':
    app.run(debug=True)
