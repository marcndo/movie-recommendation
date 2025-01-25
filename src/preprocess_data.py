# from scipy.sparse import csr_matrix

# def preprocess_data(ratings):
#     # Create a sparse matrix (user × movie)
#     user_movie_matrix = csr_matrix(
#         (
#             ratings['rating'].values, 
#             (ratings['userId'].values, ratings['movieId'].values)
#         )
#     )
#     return user_movie_matrix