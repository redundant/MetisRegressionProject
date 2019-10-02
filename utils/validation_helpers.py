import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.linear_model import LinearRegression

def split_and_validate_rmse(model, X, y, iterations=30):
    '''Given a model, features, and dependent variable, runs iterations many splits and returns the mean root mean squared error along with the standard deviation
    '''
    rmses = []
    for i in range(0,iterations):

        # perform train/val split
        X_train, X_val, y_train, y_val = \
            train_test_split(X, y, test_size=0.2)

        # fit model to training data
        model.fit(X_train, y_train)

        # score fit model on validation data
        y_pred = model.predict(X_val)
        rmses.append(np.sqrt(mean_squared_error(y_pred,y_val)))

    # report results
    return (np.mean(rmses),np.std(rmses))
