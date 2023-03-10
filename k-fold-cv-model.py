import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import TimeSeriesSplit

# load your time series data
X = np.array(...) # feature data
y = np.array(...) # target data

# Create a TimeSeriesSplit object
tscv = TimeSeriesSplit(n_splits=5)

# Initialize a linear regression model
reg = LinearRegression()

# Create an empty list to store the cross-validation scores
scores = []

# Perform k-fold cross validation
for train_index, test_index in tscv.split(X):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    
    # Fit the model on the training data
    reg.fit(X_train, y_train)
    
    # Score the model on the test data
    score = reg.score(X_test, y_test)
    
    # Add the score to the list of scores
    scores.append(score)

# Compute the mean score across all k iterations
mean_score = np.mean(scores)

# Print the mean score
print("Mean score: ", mean_score)
