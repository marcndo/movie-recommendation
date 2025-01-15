import unittest
from src.load_data import load_data
from src.preprocess_data import preprocess_data
from src.collaborative_filtering import collaborative_filtering 

class TestRecommender(unittest.TestCase):

    def test_load_data(self):
        """Test loading data from csv file."""
        ratings, movies = load_data()
        self.assertFalse(ratings.empty, "Rating data can not be empty.")
        self.assertFalse(movies.empty, 'Movies data can not be empty.')

    def test_preprocess_data(self):
        """Test for empty values in the data set."""
        ratings, _ = load_data()
        user_movie_interaction = preprocess_data(ratings)
        self.assertEqual(user_movie_interaction.isnull().sum().sum(), 0,'user_movie_interaction should contain no empty value')

    def test_collaborative_filtering(self):
        """Test the collaborative filtering logic."""
        ratings, _ = load_data()
        rmse = collaborative_filtering(ratings)
        self.assertTrue(rmse > 0, "RMSE should be positive.")

if __name__ == '__main__':
    unittest.main()