# On utilise une image python
FROM python:3.9
# On définit le répertoire de travail
WORKDIR /app
COPY app /app
# On installe les dépendances on expose le port 5000 et les infos de la db
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV DB_HOST="localhost"
ENV DB_USER="root"
ENV DB_PASSWORD=""
ENV DB_NAME="test"
# On renseigne les commandes pour démarrer l'application
CMD ["python", "app.py"]
