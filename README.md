# Movie Recommendation API Documentation

## 1. Project Overview
 ### Project Title:Movie Recommendation API
 ### Project Description:
The Movie Recommendation API is a RESTful web service built with Flask, designed to provide personalized movie recommendations based on collaborative filtering algorithms. The API predicts movie ratings for a user by analyzing the preferences of other users with similar tastes. This project uses the Surprise library, a Python-based recommendation system toolkit.

The application is a part of my portfolio showcasing my expertise in building machine learning-based applications using Flask for the backend, deploying to the cloud, and applying collaborative filtering techniques for recommendations.

Currently, the application is available for testing locally. The AWS EC2 deployment is in progress and will be available shortly.

## 2. Technologies Used
 * Python 3.x – Programming language for developing the application.
 * Flask – Lightweight web framework for building the API.
 * Surprise – Python library for building collaborative filtering models.
 * Pandas – Data manipulation library for handling datasets.
 * Numpy – Core library for numerical computations.
 * AWS EC2 (Deployment in progress) – Cloud infrastructure to deploy the application.
 * GitHub – Source code version control and collaboration platform.

## 3. How to Run the Application Locally
 ## Step-by-Step Guide:
  ### 1. Clone the Repository: Clone the repository to your local machine using the following command:
   * git clone https://github.com/marcndo/movie-recommendation.git
   * cd movie-recommendation-api
  ### 2. Install Dependencies: Set up a virtual environment (recommended for isolation) and install all the necessary Python packages:
   * python3 -m venv venv  # Create virtual environment
   * source venv/bin/activate  # Activate the virtual environment (Windows users: venv\Scripts\activate)
   * pip install -r requirements.txt  # Install required dependencies
  ## 3. Download the Dataset: The application relies on a movie ratings dataset to generate recommendations. The dataset is not stored in the repository due to its size and licensing restrictions. You can download the dataset from the following link:
   * [MovieLenz dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)
After downloading the dataset, place the ratings.csv and movies.csv files in the data/ directory of the project.
  ### 4. Run the Flask Application: Once you have the dataset and the dependencies set up, you can run the Flask application:
python app.py
The API will start running locally on http://localhost:5000.
  ### 5. Test the API Locally: You can test the API by sending requests using Postman or the curl command.
   * Example Request:
  curl "http://localhost:5000/recommend?userId=1"
   * Example Response:
     - {
       "recommendation": [
           "The Matrix",
           "Inception",
           "The Godfather",
           "Pulp Fiction",
           "The Dark Knight"
       ]
    }
  ## 4. API Endpoints Documentation
   ### API Overview:
This API exposes a GET endpoint to retrieve movie recommendations based on the user’s movie ratings history.
   - Endpoint 1: Get Movie Recommendations
    * URL:/recommend
    * Method:GET
    * Query Parameters:
     * userId (required, integer): The user ID for whom movie recommendations will be generated.
     * Example Request:
    curl "http://localhost:5000/recommend?userId=3"
     * Example Response:
       - {
       "recommendation": [
           "The Matrix",
           "Inception",
           "The Godfather",
           "Pulp Fiction",
           "The Dark Knight"
       ]
    }
  ### Error Handling:
  * 400 - Bad Request: When the userId parameter is missing or invalid.
   * Example: "error": "user id is required"
  * 404 - Not Found: When no recommendations are found for the given userId.
   * Example: "error": "No recommendation found for this user"
  * 500 - Internal Server Error: When an unexpected error occurs during the recommendation process.
   * Example: "error": "An error occurred during recommendation process"

  * 400 - Bad Request: When the userId parameter is missing or invalid.
  ## 5. Deployment - In Progress.
  #### Current Deployment Status:
   * The application is currently available for local testing only, and can be run on your local machine following the steps provided in the "How to Run the Application Locally" section.
   * Deployment to AWS EC2 is in progress. I am working on resolving a few technical issues related to AWS configuration and security settings to ensure a smooth deployment.
Once deployment is completed on AWS EC2, the application will be available for remote testing using a public IP or a custom domain name. This section will be updated as soon as the deployment is finalized.
 ## 6. Future Enhancements (Deployment Plans).
  ### AWS EC2 Deployment:
 As mentioned, the application is being actively deployed to AWS EC2 to provide a more robust and scalable solution. Once deployed, it will be accessible remotely, and I will configure an Elastic IP and custom domain name for a professional touch.
   * What’s Next:
    * fanalize deployment on AWS.
    * Add HTTPS support with SSL/TLS certificates.
    * Provide interactive API documentation using Swagger for easier interaction by potential users.
The documentation will be updated once the cloud deployment is completed, and  live API access will be provided for further testing.


