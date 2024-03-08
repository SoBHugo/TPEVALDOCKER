# TPEVALDOCKER

On fait notre cluster swarw 
Sur notre Master : docker swarm init 
Sur notre node : docker swarm join --token SWMTKN-1-03yeumuiw5gg7tgwpcv7ugogs4d9pp405ofpzq3oqw4ec4najldeik56ev6r93f8bk9rcqmo8qc 172.16.6.132:2377


On configure notre Github Actions docker-build.yml, on y configure une action qui déclenche la génération d'une nouvelle image à chaque push vers la branche principale.
Docker-build.yml
name: Build and Push Docker Image

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Build Docker image
        run: docker build -t TPEVALDOCKER/Dockerfile .

      - name: Log in to Docker Hub
        run: docker login -u ${{ secrets.DOCKER_USERNAME }} -p ${{ secrets.DOCKER_PASSWORD }}

      - name: Push Docker image
        run: docker push -t my-app-img -f TPEVALDOCKER/Dockerfile

Dans les secrets on oublie pas de renseigner le DOCKER_USERNAME et le DOCKER_PASSWORD (mes identifiants docker).

3- On stocke l'image sur docker hub





4- On déploit l'application sur le cluster docker swarm






Ensuite on crée notre Dockerfile pour construite une image docker contenant notre application


