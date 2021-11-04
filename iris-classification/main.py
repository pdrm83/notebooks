import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

iris = load_iris()

# concatenate feature variables with target
data = np.c_[iris['data'], iris['target']]
data = pd.DataFrame(data=data, columns=iris['feature_names'] + ['target'])

y = data['target']
X = data.drop(columns='target')

# partition training and testing set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# get feature selection scores
feature_selector = SelectKBest(f_classif, k=4)
feature_selector.fit(X_train, y_train)
feature_selector.pvalues_

# instantiate the model and fit it over the training set
clf = LogisticRegression(random_state=0).fit(X_train, y_train)

# predict class for new observation
new_observation = [5, 3, 5.1, 1.5]
clf.predict([new_observation])

# predict labels for testing set
y_pred = clf.predict(X_test)

accuracy_score(y_test, y_pred)
confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))