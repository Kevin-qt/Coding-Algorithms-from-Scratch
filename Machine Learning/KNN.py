import numpy as np
from collections import Counter

class KNearestNeighbors:
    '''K-Nearest Neighbors algorithm'''
    def __init__(self, k_n_neighbors=5, type='classifier'):
        self.k = k_n_neighbors
        self.type = type
    
    def fit(self, X, y):
        '''Fit the model on training data'''
        self.X = X
        self.y = y

    def predict(self, X):
        '''Make prediction on test data'''
        pred = [self._predict(x) for x in X]
        return pred
    
    def score(self, X, y_test):
        if self.type == 'classifier':
            accuracy = np.sum((self.predict(X) == y_test)/len(y_test))
            return f'Accuracy: {accuracy}'
        
        if self.type == 'regressor':
            R_squared = 1 - (np.sum((y_test - self.predict(X))**2)/np.sum((y_test - np.mean(y_test))**2))
            return f'R-squared: {R_squared}'
    
    def _predict(self, x):
        # compute the euclidean distance
        dist = [self._euclidean_distance(x, x2) for x2 in self.X]

        # find the k-nearest neighbors
        k_n_indices = np.argsort(dist)[:self.k]
        kNN = [self.y[i] for i in k_n_indices]

        if self.type == 'classifier':
            return Counter(kNN).most_common()[0][0]
            
        if self.type == 'regressor':
            return np.mean(kNN)
        
    def _euclidean_distance(self, x1, x2):
        dist = np.sqrt(np.sum((x1-x2)**2))
        return dist