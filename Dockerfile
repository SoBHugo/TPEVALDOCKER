# On utilise une image python
FROM python:3.9
# On définit le répertoire de travail
WORKDIR /app
COPY . .
# On installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt
# On renseigne les commandes pour démarrer l'application
CMD ["python", "app.py"]
