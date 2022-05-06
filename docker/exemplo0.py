"""
O que é docker, docker cria containers que são diferentes de maquinas virtuais,
enquanto maquinas virtuais precisam de s.o e configs, o docker cria containers
que virtuais tbm, porém utiliza apenas o essencial para rodar sua aplicação.

os containers são processos que ja rodam no nosso sistema operacional: esse processo cria um container, e ja tem uma s.o lá dentro.
Sistema operacional
namespace: isola os processos
Cgroups: Controla os recursos
File system: OFS (Overlay File System)

Toda container que está em execução possui uma imagem como base 
e essa imagem é imutavel,
após isso é criado o container que é READ/WRITE, porém se voce encerrar o container, 
tudo que voce alterou no container será perdido.


Como funcionam os Containers?
Através de um Dockerfile, é possível criar uma imagem, e assim criar um container usando essa imagem como base.
E para não perder as suas modificações voce pode dar um DOCKER COMMIT para salvar as alterações. porém não é o ideal e nem boa pratica
porque irá criar uma segunda imagem, e assim criar um novo container.

Como funcionam o armazenamento de imagens
As imagens criadas ficam salvas no IMAGE REGISTRY do docker que é local,
para acessar elas voce dar um docker pull se tiver criado a partir de DOCKERFILE
Se não, então voce cria a imagem com o docker build, e assim cria uma imagem nova e para usar ela
voce dar um DOCKER PUSH.  

Quando um container morre tudo se perde, e não é possível recuperar.
porém podemos compartilhar dados atraves de VOLUMES 

O que é nginx? 

Docker run -d -p 8080:80 nginx #-d para desatachar do meu terminal, -p para redirecionar a porta 8080 para 80
Docker exec nginx ls #para executar o comando dentro do container
Docker exec -it nginx bash #para executar o comando dentro do container de forma interativa entrando no bash
docker rmim nginx #para remover a imagem do cache do docker 
Docker build -t (nome do usuario/nome da imagem) . #falar o nome da imagem, . para dizer que é para pegar do diretorio atual
Docker push (nome do usuario/nome da imagem:latest)

"""