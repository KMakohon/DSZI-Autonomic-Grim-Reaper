# DSZI-Autonomic-Grim-Reaper

### Autorzy: Zofia Dobrowolska, Maciej Grochowski, Katarzyna Makohon

"Autonomiczna Kostucha" jest agentem poruszającym się po dwuwymiarowym środowisku. Jej zadaniem jest selekcjonowanie osób, które powinna zabić, oraz ustalenie optymalnej trasy, która pozwoli jej efektywnie wypełniać swoja rolę. Kostucha podejmuje decyzje, co do tego kogo i w jakiej kolejności zabić na podstawie cech indywidualnych osób (np. wiek)

---

### Autonomic Grim Reaper - Środowisko Agenta

Data: 24.03.2019

#### 1. Wstęp

W tym przyroście skupiliśmy się na stworzeniu środowiska dla agenta, oraz struktury klas wykorzystywanej w projekcie. Stworzyliśmy proste środowisko 2D stylizowane na 64Bit RPG oraz 5 klas: Game, Reaper, Person, Wall, TiledMap oraz Camera.

#### 2. Wykorzystane narzędzia

Projekt został napisany w języku Python3 przy użyciu modułu PyGame, aby wygenerować graficzną reprezentację klas, oraz umożliwić wizualizację działania agenta. Celem randomizacji parametrów wykorzystano moduł random. 

Mapa została dodana z pomocą modułu PyTMX oraz programu "Tiled", by swobodnie manipulować stworzonymi na potrzeby gry grafikami.

#### 3. Reprezentacja wiedzy

Szersze omówienie działania programu wymaga większego skupienia się na kodzie źródłowym.

- **Game:**

  Zawiera podstawowe ustawienia wyświetlania okna (wysokość, szerokość), informacje o miejscach, z których należy pobrać grafiki wykorzystywane w grze, oraz 6 metod: new(), run(), quit(), update(), draw() oraz events().

  * Metoda new() - Odpowiada za stworzenie obiektów wykorzystywanych w grze tj. Reaper, Person oraz Camera.

  * Metoda run() - Uruchamia metody events, update oraz draw w nieskończonej pętli.

  * Metoda quit() - Odpowiada za zamknięcie gry i zakończenie programu. 

  * Metoda update() - Uruchamia metody update wszystkich sprite'ów celem zaktualizowania ich pozycji. 

  * Metoda draw() - Odpowiada za umieszczenie na mapie sprite'ów.

  * Metoda events() - W obecnym kształcie sprawdza czy użytkownik nie chce wyłączyć programu. Gdy użytkownik wciśnie klawisz Escape, lub zamknie okno programu, uruchamia metodę quit().

- **Reaper:**

  Jest obiektem zawierającym sprite postaci agenta. Posiada paramtery pozwalajace umieścić go w przestrzeni oraz informacje odnośnie gry. Posiada metodę get_keys() oraz update().

  * Metoda get_keys() - Oczekuje na event (tj. naciśnięcie przez gracza któregoś z klawiszy strzałek) a następnie tworzy wektor wykorzystywany przez metodę update() do zmiany pozycji agenta w przestrzeni. W przypadku zmiany kierunku ruchu zmienia również obrazek przypisany agentowi.  

  * Metoda update() - zmienia paramtery agenta i jego pozycję na mapie. 

- **Person:**

  Jest to obiekt zawierający sprite postaci z którą agent w przyszłości wejdzie w interakcję. Posiada ona parametry pozwalające umieścić ją w środowisku agenta, oraz parametry opisujące wiek, choroby, charakter i płeć. Postać nie ma opcji poruszenia się.

- **Wall:**

  Klasa określa obiekty, które agent będzie postrzegał jako przeszkody.  Posiada parametry umieszczające przeszkodę w przestrzeni oraz parametry określające wysokość i szerokość przeszkody. 

- **TiledMap:**

  Jest to klasa tworząca mapę na podstawie przygotowanego wcześniej w programie "Tiled" pliku.

- **Camera:**

  Jest to klasa stworzona po to, aby postać agenta zawsze była widoczna na ekranie. Posiada ona parametry pozwalające umiejscowić ją w środowisku oraz metody pozwalające zmieniać jej pozycję. 

---


