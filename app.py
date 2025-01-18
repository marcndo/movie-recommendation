from flask import Flask, request, jsonify
from src.recommender import collaborative_filtering, load_data, preprocess_data, get_recommendation

app = Flask(__name__)

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('userId', type=int)
    if not user_id:
        return jsonify({'error':'user id is required'}), 400
    
    #Load data
    ratings, movies = load_data()
    
    #Process and build model
    user_movie_interaction = preprocess_data(ratings)
    algo = collaborative_filtering(ratings)
    
    # Generate recommendations using collaborative filtering
    recommendation = get_recommendation(user_id, algo, movies, ratings)

    return jsonify({"recommendation":recommendation})

if __name__ == '__main__':
    app.run(debug=True)
