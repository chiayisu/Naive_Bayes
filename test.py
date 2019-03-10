import Classifier
import numpy as np
import pandas as pd
NB = Classifier.NaiveBayes()
train_features = np.array([[1, 2, 2, 3], [1,3,2,1], [1, 2, 2, 3]])
label = np.array([1, 1, 0])
NB.train(features = train_features, label = label)
features = np.array([[0,1,0,0], [1,2,1,2]])
cat, prob = NB.predict(features = features)
print('category = ', cat)
print('each probability = ', prob)
