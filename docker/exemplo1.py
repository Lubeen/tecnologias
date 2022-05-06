'''
docker comandos importantes

docker run ubuntu #irá baixar a imagem do ubuntu(inicia o container)

docker run (alguma coisa)#vai baixar a imagem, mas nao vai executar o processo

docker ps #lista as imagens que estão rodando

docker ps -a #lista as imagens que estão rodando e as que não estão

docker run -p 8080:80 (alguma coisa)#vai rodar a imagem e vai abrir a porta 8080, mas vai redirecionar para 80

docker exec name_container echo "<h1>Hello</h1>" >> /usr/share/nginx/html/index.html (executa um comando dentro do container)

docker exec -it name_container bash (executa um comando dentro do container) #it modo iterativo para executar comandos dentro do container com bash

docker images #lista as imagens que estão disponíveis no docker

docker images -a #lista as imagens que estão disponíveis no docker e as que não estão

docker rmi (alguma coisa)#remove a imagem

docker rmi -f (alguma coisa)#remove a imagem e se tiver alguma dependencia, também remove

docker run -d -p 8080:80 (alguma coisa)#vai rodar a imagem e vai abrir a porta 8080, mas não vai utilizar o meu terminal, vai executar no -d

docker build -t (usuario:dockerhub/alguma coisa) . #vai criar uma imagem, o ponto para dizer que é no mesmo diretorio

docker run -d -p 8080:80 (alguma coisa)#vai rodar a imagem e vai abrir a porta 8080, mas não vai utilizar o meu terminal, vai executar no -d

docker push (usuariohub/alguma coisa)#vai mandar para o dockerhub

docker pull (usuariohub/alguma coisa)#vai baixar da dockerhub

docker -compose up -d #vai rodar o docker-compose e nao vai executar no meu terminal

docker -compose down #vai parar o docker-compose

cat /etc/hosts #quando voce quer acessar sua maquina dentro de um container ai voce passa a porta

'''