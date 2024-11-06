# Lab4

## Opis projektu
Ten projekt to aplikacja napisana w Pythonie, która analizuje dane z pliku `CollegeDistance.csv` i wykorzystuje model uczenia maszynowego do przewidywania określonych wyników.

## Wymagania
- Python 3.8 lub nowszy
- Docker (opcjonalnie, jeśli chcesz uruchomić aplikację w kontenerze)

## Instalacja

### 1. Klonowanie repozytorium
```bash
git clone https://github.com/s25211/Lab4.git
cd Lab4
```

### 2. Tworzenie i aktywacja wirtualnego środowiska (opcjonalnie, ale zalecane)
```bash
python -m venv venv
source venv/bin/activate  # Na systemach Unix/Linux/Mac
# lub
venv\Scripts\activate  # Na systemach Windows
```

### 3. Instalacja zależności
```bash
pip install -r requirements.txt
```

## Uruchomienie aplikacji

### 1. Przygotowanie danych
Upewnij się, że plik `CollegeDistance.csv` znajduje się w głównym katalogu projektu.

### 2. Uruchomienie skryptu
```bash
python main.py
```
Skrypt wczyta dane, przetworzy je i wyświetli wyniki na standardowym wyjściu.

## Uruchomienie aplikacji w Dockerze
Jeśli preferujesz uruchomienie aplikacji w kontenerze Docker, wykonaj następujące kroki:

### 1. Budowanie obrazu
```bash
docker build -t lab4-app .
```

### 2. Uruchomienie kontenera
```bash
docker run --rm -v $(pwd):/app lab4-app
```
Powyższa komenda uruchomi kontener, który wykona skrypt `main.py` i wyświetli wyniki.

## Struktura projektu
- `main.py` – główny skrypt aplikacji
- `CollegeDistance.csv` – plik z danymi wejściowymi
- `best_model.pkl` – zapisany model uczenia maszynowego
- `requirements.txt` – lista zależności Pythona
- `Dockerfile` – plik konfiguracyjny dla Dockera

## Uwagi
- Upewnij się, że masz zainstalowane wszystkie wymagane zależności przed uruchomieniem aplikacji.
- Jeśli napotkasz problemy z uruchomieniem aplikacji w Dockerze, sprawdź, czy masz zainstalowaną najnowszą wersję Dockera i że demon Dockera jest uruchomiony.

Jeśli masz dodatkowe pytania lub potrzebujesz pomocy, skontaktuj się z autorem projektu.
