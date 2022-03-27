import numpy as np
import pandas as pd

training_data = pd.read_csv('storepurchasedata.csv')

training_data.describe()

X = training_data.iloc[:, :-1].values
y = training_data.iloc[:, -1].values
np.random.seed(0)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .20, random_state=0)

# Scale the models change it to numpy format
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

"""
## Build a Classification model
### We are using KNN Classifier in this example
* n_neighbors = 5 -* Number of neighbors
* metic = 'minkowski', p = 2* - for Eucledian distance calculation
"""

# KNN Model turn it to 0s and 1s
from sklearn.neighbors import KNeighborsClassifier
# minkowski is for ecledian distance - shortest distance between two points
classifier = KNeighborsClassifier(n_neighbors=5, weights='uniform', algorithm='auto', leaf_size=30, p=2, metric='minkowski', metric_params=None, n_jobs=None)

# // Model training
classifier.fit(X_train, y_train)

# Predict data
y_pred = classifier.predict(X_test)
# Check probability of test data
y_prob = classifier.predict_proba(X_test)[:,1]

#Confusion matrix can be use to calculate the accuracy of the model
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)

# Let' calculate the accuracy of the model
from sklearn.metrics import accuracy_score

score = accuracy_score(y_test, y_pred)
score

# Classification Report to see precision, F1-score, Recall, support
from sklearn.metrics import classification_report 
cls_report = classification_report(y_test, y_pred)
cls_report

# Try a new prediction with age=40, salary 20000, if customer will but, predict not buy

new_prediction = classifier.predict(sc.transform(np.array([[40,20000]])))

new_prediction_proba = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]

new_pred = classifier.predict(sc.transform(np.array([[42,50000]])))

new_pred_proba = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]

# save model to file using Pickle
import pickle
model_file = "classifier2.pickle"
# save model classifier  'wb' is writing in binary
pickle.dump(classifier, open(model_file, 'wb'))
# save the scale file
scaler_file = "sc2.pickle"
pickle.dump(sc, open(scaler_file, 'wb'))











