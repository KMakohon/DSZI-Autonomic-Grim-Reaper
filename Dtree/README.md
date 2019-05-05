# DSZI-Autonomic-Grim-Reaper

### Autorzy: Zofia Dobrowolska, Maciej Grochowski, Katarzyna Makohon

"Autonomiczna Kostucha" jest agentem poruszającym się po dwuwymiarowym środowisku. Jej zadaniem jest selekcjonowanie osób, które powinna zabić, oraz ustalenie optymalnej trasy, która pozwoli jej efektywnie wypełniać swoja rolę. Kostucha podejmuje decyzje, co do tego kogo i w jakiej kolejności zabić na podstawie cech indywidualnych osób (np. wiek)

---

### Autonomic Grim Reaper - Podprojekt indywidualny - Drzewo decyzyjne

**Zofia Dobrowolska**

Data: 05.05.2019

#### 1. Wstęp

W tym przyroście skupiłam się na stworzeniu drzewa decyzyjnego, którego zadaniem bedzie decydowanie czy kostucha powinna zabić czy oszczędzić daną osobę na podstawie paramertów przypisanych do osoby (objektu klasy Person). Atrybuty te ('gender', 'age', 'disease', 'good', 'lawful', 'money') są zmiennymi liczbowymi.

#### 2. Wykorzystane narzędzia

Podprojekt indywidualny został napisany w języku Python3 przy użyciu modułu **decision-tree-id3** do stworzenia drzewa przy użyciu wbudowanego w moduł algorytmu id3 oraz wygenerowania pliku .dot, **Pandas** do szczytywania danych treningowych dla drzewa z pliku dane.csv, **Sklearn** do podziału danych na dane testowe oraz treningowe i obliczenia średniej poprawności drzewa oraz programu **Graphviz** do wizualizującji wygląd drzewa i korzystającego z wygenerowanego pliku .dot.

#### 3. Zmiany

Powstał katalog Dtree zawierający natępujące pliki:

- Dtree.py - plik zawierający implementacje drzewa
- dane.csv - plik zawierający przykłady dla drzewa. Przykłady są formacie ['gender', 'age', 'disease', 'good', 'lawful', 'money', 'dead']. Kolumna 'dead' jest kolumną zawierającą przewidywany wynik (0 - żywa, 1 - martwa). Cała reszta odpowiada nazwami atrybutom klasy Person. Przykład: ("1","22","10","100","34","886","1").
- Dtree.dot - plik wygenerowany przez Dtree.py i obsługiwany przez program Graphviz.
- Dtree.png - wizualizacja drzewa wygenreowana z pliku Dtree.dot przez program Graphviz.

#### 4. Drzewo decyzyjne

Główną częścią podprojektu jest plik Dtree.py implementujący drzewo decyzyjne. Plik zawiera następujące funkcje:

- pd.read_csv("dane.csv", header=None, names=names) - Szczytująca zawartość pliku .csv. Jako argumenty bierze nazwę pliku, którego zawartość ma zostać szczytana oraz dodatkowe atrybuty jak header=None czyli nie wyświetlanie pierwszej linijki jako nagłówka z nazwami oraz names=**names** zawierający nazwy kolumn. **names** to tablica stringów, która zawiera zawiera nazwy odpowiadajace poszczególnym kolumnom. Wyniki operacji zapisuje się w zmiennej **dataset**

- Id3Estimator() - Tworzy generator drzew decyzyjnych opierajac się o algorytm Id3 i przypisuje go do zmiennej **estimator**.

- dataset['dead'] - Przypisuje do zmiennej **y** wszystkie dane z kolumny "dead"

- dataset.drop('dead', axis=1) -  Przypisuje do zmiennej **X** wszystkie dane z wszystkich kolumn poza kolumną "dead"

- train_test_split(X, y, test_size=0.20) - Funkcja mająca za zadanie rodzielić całość posiadanych przykładów na dane treningowe dla drzewa oraz dane testowe (20%- dane testowe, 80% danye treningowe). Argumentami są X oraz y (podane wyżej)  oraz liczba  0 <= test_size <=  1 oznaczającą jakim procentem wszystkich danych mają być dane testowe. Dane testowe zostaną zapisane do zmiennych **X_test** i **y_test**, a dane treningowe do zmiennych **X_train** i **y_train**

- estimator.fit(X_train, y_train) - Tworzy drzewo decyzyjne z wcześniej wygenrowanych danych treningowych.

- estimator.predict(X_test) - Na postawie wygenrowanego drzewa funkcja przewiduje wyniki dla zbioru testowego. 

- confusion_matrix(y_test, y_pred) - Tworzy macierz błędu na podstawie wyników danych testowych, a podanych wyników danych treningowych.

- classification_report(y_test, y_pred) - Pokazuje średnią procentową poprawność przewidywań drzewa decyzyjnego na podstawie wyników danych testowych, a podanych wyników danych treningowych.

- export_graphviz() - generuje plik .dot dla programu graphviz.
