# Użyj lekkiego obrazu bazowego Pythona
FROM python:3.9-slim

# Ustaw katalog roboczy
WORKDIR /app

# Skopiuj plik z zależnościami (jeśli posiadasz)
COPY requirements.txt .

# Zainstaluj zależności
RUN pip install --no-cache-dir -r requirements.txt

# Skopiuj resztę plików aplikacji
COPY . .

# Expose port aplikacji
EXPOSE 5000

# Uruchom aplikację
CMD ["python", "app.py"]
