import pickle
import numpy as np

np.random.seed(0)
# load saved classifier model using pickle --rb is read binary
classifier = pickle.load(open('classifier.pickle', 'rb'))
# load saved scaler
sc = pickle.load(open('sc.pickle', 'rb'))
# use loaded model to predict

new_pred1 = classifier.predict(sc.transform(np.array([[40,20000]])))

new_pred_proba1 = classifier.predict_proba(sc.transform(np.array([[40,20000]])))[:,1]

new_pred2 = classifier.predict(sc.transform(np.array([[42,50000]])))

new_pred_proba2 = classifier.predict_proba(sc.transform(np.array([[42,50000]])))[:,1]

