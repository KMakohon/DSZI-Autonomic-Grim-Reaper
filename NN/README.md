# DSZI-Autonomic-Grim-Reaper

### Autorzy: Zofia Dobrowolska, Maciej Grochowski, Katarzyna Makohon

"Autonomiczna Kostucha" jest agentem poruszającym się po dwuwymiarowym środowisku. Jej zadaniem jest selekcjonowanie osób, które powinna zabić, oraz ustalenie optymalnej trasy, która pozwoli jej efektywnie wypełniać swoja rolę. Kostucha podejmuje decyzje, co do tego kogo i w jakiej kolejności zabić na podstawie cech indywidualnych osób (np. wiek)

---

### Autonomic-Grim-Reaper - Podprojekt indywidualny, Sieć Neuronowa

**Maciej Grochowski**

### Wstęp

W projekcie indywidualnym utworzyłem prostą sieć neuronową, zajmującą się rozpoznawaniem obrazu. Na planszy gry istnieje o wiele więcej rodzajów obiektów (owoce, pojazdy, ludzie, zwierzęta). Zadaniem kostuchy jest zabijanie ludzi, toteż musi ona ich rozpoznawać. W obecnym stanie kostucha może poruszać się po planszy, a kiedy zetknie się z postacią - ocenia jej typ po obrazie. Jeżeli obiekt jest człowiekiem, o jego życiu i śmierci może zadecydować zintegrowane z resztą aplikacji drzewo decyzyjne (przedstawiane wcześniej).
Dla prezentacji działania sieci neuronowej, gdy dochodzi do spotkania kostuchy z obiektem (obrazowanym na mapie jako człowiek - choć wcale człowiekiem być nie musi), w osobnym okienku ukazuje się obrazek, a w konsoli werdykt o typie obiektu. Dodatkowo obiekty generowane są częściowo losowo (losowe położenie oraz częściowo losowy typ).

---

### Struktura Podprojektu

Podprojekt został wykonany dzięki modułowi torch. Do pobieranie i kontrolowania danych został wykorzystany moduł torchvision; prócz tego użyte zostały inne podmoduły modułu torch, moduł numpy, a także moduł matplotlib (umożliwiający pokazywanie obrazów na ekranie.)

Podprojekt został podzielony na kilka plików, obecnych w podfolderze NN. Są to:

**LearningNeuralNetwork.py** - plik odpowiedzialny za nauczanie sieci neuronowej. Zawiera definicję klasy Net (dziedziczącej po nn.Module z modułu Torch), definicję zbioru testowego, funkcję test() (służącą do testowania rozpoznawania kilku obrazów), a także m.in. funkcje success() i getstats(), dającą dostęp do statystyk skuteczności sieci neuronowej. Poruszanie się po programie zostało zaimplementowane w prosty sposób, z użyciem konsoli i kilku podstawowych komend.

**LearnedNetwork.pt** - plik, w którym zapisano wyuczoną sieć neuronową. Nie jest plikiem wykonywalnym, zawiera jedynie dane możliwe do wgrania przez dowolny obiekt klasy Net.

**NeuralNetwork.py** - plik odpowiedzialny za działanie już wyuczonej sieci neuronowej. Jest zaimplementowany w kilku spośród dotychczasowych plików kostuchy. Implementuje m.in. funkcję load, służącą do wgrania danej sieci neuronowej z pliku .pt, funkcję imshow(), służącą do pokazywania obrazków w formie czytelnej dla człowieka, a także funkcję predictImg(), pozwalającą przewidzieć typ danego obrazka.

---

### Zmiany

Dotychczasowe pliki nie zmieniły się znacząco. Godnym odnotowania jest fakt, że klasa Game zawiera od teraz także pole net - jest to wgrana sieć neuronowa. Dodatkowo klasa person.py zawiera od teraz w sobie obrazek, przedstawiający dany obiekt, niekoniecznie osobę. Dodatkowo zaimplementowano prostą metodę banish(), zajmującą się zabijaniem napotkanego człowieka, jeśli nie spełnia on wyznaczonych przez drzewo decyzyjne standardów.

---

### Zbiór danych i skuteczność

Użytym przeze mnie zbiorem danych był CIFAR-100 - popularny zbiór danych, posiadający łącznie 60000 obrazków, w rozdzielczości 32x32 pikseli, podzielonych na 20 superklas (m.in. people, trees, flowers). Każda superklasa zawiera 5 podklas (np. "people" -> "baby", "boy", "girl", "man", "woman"), co łącznie daje 100 klas. Każda klasa zawiera 600 obrazków, w tym 500 treningowych oraz 100 testowych.
Skuteczność osiągnięta przez moją sieć wynosi około **55%**. Najlepsze osiągane przez sieć neuronową wyniki oscylują wokół 90%, jednak z uwagi na sprzęt/czas uczenia, różnica ta jest zrozumiała.

---

### Użyte techniki, narzędzia i operacje

**Konwolucyjna Sieć Neuronowa** - jest to warstwowa architektura sieci, w której na wartość danego neuronu w warstwie następnej mają wpływ nie wszystkie neurony z warstw poprzednich, a jedynie lokalna informacja z pewnego sąsiedztwa danego piksela. Operację tę można interpretować jako wstępne filtrowanie. W mojej sieci występują dwie warstwy konwolucyjne, każda złożona z 5 kanałów.

**Liniowa Sieć Neuronowa** - w projekcie występują także trzy warstwy tradycyjnej, liniowej sieci neuronowej.

**Pooling** - operacja poolingu polega na wyciągnięciu jak najważniejszej informacji z danego obszaru obrazu, co pozwala efektywnie zmniejszyć jego rozmiar, a co za tym idzie uprościć obliczenia. W mojej sieci neuronowej zaimplementowałem pooling efektywnie zmniejszający oceniane obrazki dwukrotnie.

**Funkcja aktywacji** - jako funkcję aktywacji sieci neuronowej ustaliłem funkcję "rectified linear unit" (ReLU), definiowaną następująco: **f(x) = max(0,x)**

**Funkcja straty** - używana jako ocena modelu, informująca o ilości popełnianych błędów, oraz interpretująca istniejący model sieci jako "dobry"(niski output funkcji) lub "zły"(wysoki output funkcji). W moim algorytmie wykorzystałem funkcję CrossEntropyLoss, zaimplementowaną w module Torch.

**Algorytm optymalizyjny - SGD** - Metoda Najszybszego Spadku (Stochastic Gradient Descent) łączona jest z funkcją straty celem poszukiwań takich wartości wag, w których funkcja straty będzie najniższa, tzn. skuteczność największa. 

**Algorytm wstecznej propagacji błędu** - określa procedurę
korekty wag w sieci wielowarstwowej. Polega na "przenoszeniu" błędu jaki popełniła sieć, z warstwy wyjściowej, do warstwy wejściowej.

---

### Podsumowanie

Po zintegrowaniu, aplikacja zaczyna przypominać autonomiczną. Mając na planszy dowolną liczbę obiektów, kostucha potrafi ocenić, które z nich są ludźmi, a następnie wybrać spośród stworzonej kolekcji ludzi tych, których należy zabić. Implementacja ruchu kostuchy zostaje pozostawiona trzeciemu spośród podprojektów - algorytmowi genetycznemu.








































