from surprise import accuracy

def evaluate_model(prediction):
    """Evaluate the performance of the model"""
    rmse = accuracy.rmse(prediction)
    print(f'RMSE: {rmse}')
    return rmse