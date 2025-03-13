# Movie Recommendation API Documentation

## 1. Project Overview
 ### Project Title:Movie Recommendation API
 ### Project Description:
The Movie Recommendation API is a RESTful web service developed using Flask and Surprise (a Python-based recommendation system library), designed to deliver personalized movie recommendations. The application leverages collaborative filtering algorithms to predict movie ratings based on user preferences, providing a highly customized user experience. This project demonstrates my ability to build and deploy machine learning-powered applications, with a focus on scalable web services and cloud deployment.

### Key Features:

+ Collaborative Filtering: Utilizes collaborative filtering algorithms to generate movie recommendations based on the preferences of similar users.
+ RESTful API: Exposes a well-documented API to interact with the recommendation system, allowing easy integration with front-end interfaces or other applications.
+ Machine Learning Integration: Implements Surprise for collaborative filtering, showcasing proficiency in machine learning algorithms and data handling.
+ Flask Framework: Built with Flask, a lightweight Python framework, to create a modular and scalable backend architecture.
+ Cloud Deployment (AWS): The application is currently being deployed on AWS EC2, with ongoing work to make the service publicly accessible.
### Project Goals:
+ Personalized User Experience: By implementing collaborative filtering, the API predicts user preferences for movies, allowing the system to suggest relevant titles.
+ Scalability and Deployability: The project is designed with scalability in mind, utilizing Flask for the backend and setting up cloud infrastructure to support future traffic and growth.
+ Machine Learning: Provides hands-on experience with machine learning techniques like collaborative filtering and model deployment in real-world applications.
---

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
 ```bash
  git clone https://github.com/marcndo/movie-recommendation.git
  cd movie-recommendation-api
   ```
  ### 2. Install Dependencies: Set up a virtual environment (recommended for isolation) and install all the necessary Python packages:
  ```
   python3 -m venv venv
   Create virtual environment.
   source venv/bin/activate
   Activate the virtual environment (Windows users: venv\Scripts\activate)
   pip install -r requirements.txt
   Install required dependencies
   ```
  ## 3. Download the Dataset: The application relies on a movie ratings dataset to generate recommendations. The dataset is not stored in the repository due to its size. You can download the dataset from the following link:
   * [MovieLenz dataset](https://www.kaggle.com/datasets/grouplens/movielens-20m-dataset)
After downloading the dataset, place the ratings.csv and movies.csv files in the data/ directory of the project.
  ### 4. Run the Flask Application: Once you have the dataset and the dependencies set up, you can run the Flask application:
```bash
python app.py
```
The API will start running locally on http://localhost:5000.
  ### 5. Test the API Locally: You can test the API by sending requests using Postman or the curl command.
   * Example Request:
 ```bash
  curl "http://localhost:5000/recommend?userId=1"
 ```
   * Example Response:
     ```
     - {
       "recommendation": [
           "The Matrix",
           "Inception",
           "The Godfather",
           "Pulp Fiction",
           "The Dark Knight"
       ]
    }
    ```
  ## 4. API Endpoints Documentation
   ### API Overview:
This API exposes a GET endpoint to retrieve movie recommendations based on the user’s movie ratings history.
   - Endpoint 1: Get Movie Recommendations
    * URL:/recommend
    * Method:GET
    * Query Parameters:
     * userId (required, integer): The user ID for whom movie recommendations will be generated.
     * Example Request:
    ```bash
    curl "http://localhost:5000/recommend?userId=3"
    ```
  
     * Example Response:
       ``` {
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

    
  ## 5 Project Status.
  + Local Testing: The API is currently functional and available for local testing, allowing users to experiment with personalized movie recommendations.
  + Cloud Deployment: Deployment on AWS EC2 is in progress, and the application will be live soon, providing real-time recommendations in a production environment.


 ## 6. Future Work
+ Enhanced Recommendation Algorithm: Integrating additional filtering methods and hybrid recommendation strategies to improve prediction accuracy.
+ Front-End Integration: Developing a front-end interface (e.g., with React or Angular) to interact with the API and visualize movie recommendations.
+ Real-Time Data Updates: Implementing a mechanism for real-time updates and continuous improvement of the recommendation model with fresh data.


 



