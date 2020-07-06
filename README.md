# ProjetoPython

![Fatec Osasco](imgPgit/ftFatec.jpg)

#### Projeto proposto pelo professor Flavio na Fatec Osasco

###### Deve-se realizar produção do sistema de uma urna eletrônica.

![urna eletrônica](imgPgit/urna.jpg)

------------------------------------------------------------------

## Linguagem

- Python

## Requisito de software

- Python3 em diante

## Banco de Dados

- sqlite3

## Paradigmas de programação

- Orientado á objeto
- Procedural

------------------------------------------------------------------

## Documentação

### Documentação do sistema

Ao iniciar o programa, é mostrado o Menu de longins. A parir dai pode-se logar como qualquer permição do sistema(Administrador, Presidente,Scretario, Mesario).
Para se logar como Administrador é nescessario o nome "root" e a senha é "123", a partir dessa permição é possivel cadastrar um secretario, ver os Secretarios cadstrados, recuperar a senha de algum Secretario e voltar ao menu principal, para se logar com outras permições.
Ao se logar como Secretario pode-se cadastrar Presidentes, Mesarios ou Candidatos, pode-se também mostrar destes os que estão cadastrados e voltar ao menu principal.
Como Presidente é possivel limpar os dados do banco para iniciar a votação, mostrar os eleitores, fechar a eleição e computar votos, e voltar ao menu principal.
Como Mesario pode-se liberar a votação para os eleitores e voltar para o nivel presidente.
Os eleitores precisam digitar o seu CPF, seu nome e depois da demonstração dos candidatos cadstrados no sistema, pergunta-se em quem se deseja votar e depois disso cadstra-se o eleitor no sistema.

### Documentação das classes

###### os metodos que não estão especificados não passa-se atributos

##### Métodos da classe menuPrincipal

- menu: mostra o menu principal
- loginSecretario: Loga como secretario. Passa como atributo nome e senha do usuario.
- loginPresidente: Loga como Presidente. Passa como atributo o nome e senha para o presidente.
- loginMesario: Loga como Mesario. Passa como atributo o nome e senha para o mesario.

##### Métodos da classe administrador

- menu: Mostra o menu de administrador.
- mostraSecretarios: Mostra os secretarios cadastrados no banco.
- inserirSecretario: insere um novo secretario no banco. Passa como atributo nome do secretario e a senha.
- recuperaSenha: Pede o nome e mostra a senha do usuario cadstrado no banco. Passa como atributo nome do secretario.

##### Métodos da classe secretario

- menu: Mostra o menu de secretario.
- inserirPessoa: Serve tanto para inserir um Mesario quanto um Presidente, pois pede o serviço que será realizado pelo novo usuario cadstrado. Passa como atributo o nome, senha e serviço do usuario a ser cadastrado.
- inserirCandiato: Serve para inserir um candidato para ser votado, pede o numero que será oque os eleitores irão votar.Passa como atributo o numero a ser votado, nome e função que esta se elegendo.
- mostrarMesariosPresidentes: Serve para mostrar os mesarios e presidentes cadastrados.
- mostrarCandidatos: mostra os candidatos cadastrados no sistema.

##### Métodos da classe presidente

- menu: Mostra o menu para presidente.
- inicioVotacao: Limpa os votos atuais e inicia a votação
- computarVotos: Computa os votos nos candidatos.
- mostarEleitores: mostra os Eleitores que votaram.

##### Métodos da classe mesario

- menu: Mostra o menu para mesario.
- inserirEleitor: Insere o eleitor no banco de dados Passa como atributo o cpf, nome e voto do eleitor.

------------------------------------------------------------------

## Sobre os arquivos

- urna.py --> Contem as classes, atributos, métodos e tabelas do banco de dados (Orientado á objeto)
- main.py --> É o arquivo que chama os métodos das classes no programa (Procedural)
