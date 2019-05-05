import pandas as pd
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split  # Import train_test_split function
from id3 import Id3Estimator
from id3 import export_graphviz

#nazwy kolumn (dead :1 -umrze, 0 - przeżyje)
names = ['gender', 'age', 'disease', 'good', 'lawful', 'money', 'dead']
Nfeature_names = ['gender', 'age', 'disease', 'good', 'lawful', 'money']

# wczytaj dataset z pliku dane.csv
dataset = pd.read_csv("dane.csv", header=None, names=names)
print(dataset.head())  # show first 5 rows

print ("Dataset Lenght:: ", len(dataset))
print ("Dataset Shape:: ", dataset.shape)

estimator = Id3Estimator()

X = dataset.drop('dead', axis=1)
y = dataset['dead']

#Podział na dane treningowe i dane testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
estimator.fit(X_train, y_train)

#średnia poporawność i macież błędu
y_pred = estimator.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))

#tworzenie pliku Graphviz
export_graphviz(estimator.tree_, 'Dtree.dot', Nfeature_names)
