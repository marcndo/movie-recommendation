from flask import Flask, request, jsonify
from src.recommender import collaborative_filtering, load_data

app = Flask(__name__)

@app.rout('/recommend', methods=['GET'])
def recommend():
    user_id = request.args.get('user_id', type=int)

    #Load data
    ratings, movies = load_data()
    
    # Generate recommendations using collaborative filtering
    rmse = collaborative_filtering(ratings)
    return jsonify({"message":"Recommendation generated successfully", "RMSE":rmse})

if __name__ == '__main__':
    app.run(debug=True)
