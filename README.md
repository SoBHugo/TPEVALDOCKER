# TPEVALDOCKER

On fait notre cluster swarw 
Sur notre Master : docker swarm init 
Sur notre node : docker swarm join --token SWMTKN-1-03yeumuiw5gg7tgwpcv7ugogs4d9pp405ofpzq3oqw4ec4najldeik56ev6r93f8bk9rcqmo8qc 172.16.6.132:2377



On configure notre Github Actions docker-build.yml, on y configure une action qui déclenche la génération d'une nouvelle image à chaque push vers la branche principale.



Dans les secrets on oublie pas de renseigner le DOCKER_USERNAME et le DOCKER_PASSWORD (mes identifiants docker).




Ensuite on crée notre Dockerfile pour construite une image docker contenant notre application


docker build -t sobhugo/mon-conteneur:latest .




4- On déploit l'application sur le cluster docker swarm
on décrit le dploiement de notre app swarm dans docker-compose.yml

Puis on déploit notre application sur le Swarm


docker stack deploy -c sobhugo/mon-conteneur:latest






