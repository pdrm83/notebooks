import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from xgboost.sklearn import XGBClassifier


df = pd.read_json('c:\\Users\\Admin\\Repositories\\data_science_interview\\classification\\diabetes\\data.json')
df_mod = df.drop(columns=['SkinThickness','Insulin'], axis=1)

features = df_mod[['DiabetesPedigreeFunction','BloodPressure','Pregnancies','BMI','Age', 'Glucose']]
outputs = df[['Outcome']]

outputs = outputs.astype('float64')
features = features.astype('float64')

sc = StandardScaler()
features_norm = sc.fit_transform(features)
outputs_mod = outputs.to_numpy().flatten()
x_train, x_test, y_train, y_test = train_test_split(features_norm, outputs_mod)

xgb = XGBClassifier(use_label_encoder=False, eval_metric=["error"])
xgb.fit(x_train, y_train)

y_pred = xgb.predict(x_test)
k_fold = KFold(n_splits=10, shuffle=True)
score = cross_val_score(xgb, x_train, y_train, cv=k_fold, scoring='accuracy')
print('Mean:', score.mean(),'Std:', score.std())