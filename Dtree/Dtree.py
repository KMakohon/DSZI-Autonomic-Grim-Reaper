import pandas as pd
from id3 import Id3Estimator
from sklearn.model_selection import train_test_split

def BuildTree():

    #nazwy kolumn (dead :1 -umrze, 0 - przeżyje)
    names = ['gender', 'age', 'disease', 'good', 'lawful', 'money', 'dead']
    Nfeature_names = ['gender', 'age', 'disease', 'good', 'lawful', 'money']

    # wczytaj dataset z pliku dane.csv
    dataset = pd.read_csv("Dtree/dane.csv", header=None, names=names)

    X = dataset.drop('dead', axis=1)
    y = dataset['dead']

    #tworzenie drzewa
    estimator = Id3Estimator()

    #Podział na dane treningowe i dane testowe
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    estimator.fit(X_train, y_train)

    #średnia poporawność i macież błędu
    y_pred = estimator.predict(X_test)
    return estimator

def PredictDead(victim, estimator):
    victimInfo = [[victim.gender, victim.age, victim.disease, victim.good, victim.lawful, victim.money]]
    result = estimator.predict(victimInfo)
    print(result)
    return result