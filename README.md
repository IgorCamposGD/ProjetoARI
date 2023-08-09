# ProjetoARI
Este é um projeto que utiliza a lib ARI da liguagem python que realiza o controle da ligação quando chamado a aplicação pelo asterisk.

# Pré-requisitos:
Antes de começar, certifique-se de ter o Docker instalado em seu sistema. Se você ainda não tem o Docker instalado, siga as instruções em https://docs.docker.com/get-docker/ para instalar a versão adequada ao seu sistema operacional.

Antes de começar a executar o projeto, altere dentro de docker-python > env.py a variavel de ambiente HOST para seu IP LOCAL e também em docker-asterisk ajustar dentro de pjsip.conf o NAT de acordo com a rede do docker e o seu ip local.

Executando o projeto
Para executar o projeto, siga os seguintes passos:

**1 - Clone o repositório para o seu ambiente local:**

```bash
git clone https://github.com/IgorCamposGD/ProjetoARI
```

**2 - Acesse o diretório do projeto:**

```bash
cd ProjetoARI
```

**3 - Em seguida, você pode executar o comando(deixando-o em execução em segundo plano (deixando-o em execução em segundo plano (-d)):**

```bash
docker-compose up -d
```

Agora voce pode acessar o linux com o comando:

```bash
docker exec -it asterisk bash
```

Para realizar os teste basta registrar um ramal pegando a autenticação no pjsip.conf e ligar para a ura 100 se voce digite 1, voce será encaminhado para extensão 200 e vai executar um audio informando "lamentamos", e caso digite 2 será um audio dizendo "dia"(esses audios foram escolhido aleatoriamente por mim, voce pode altera-lo caso deseje no extensions.conf).