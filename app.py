from flask import Flask, request, jsonify
from src.recommender import collaborative_filtering, load_data, get_recommendation

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World!"

@app.route('/recommend', methods=['GET'])
@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('userId', type=int)
    if not user_id:
        return jsonify({'error': 'user id is required'}), 400

    try:
        ratings, movies = load_data()
        algo = collaborative_filtering(ratings)
        recommendation = get_recommendation(user_id, algo, movies, ratings)

        if not recommendation:
            return jsonify({'error': 'No recommendation found for this user'}), 404
        
        return jsonify({"recommendation": recommendation})
    
    except ValueError as ve:
        return jsonify({'error': str(ve)}), 404  # User ID not found
    
    except Exception as e:
        print(f"Error during recommendation: {e}")


if __name__ == '__main__':
    app.run(debug=True)
