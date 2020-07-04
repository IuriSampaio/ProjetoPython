# ProjetoPython
![Fatec Osasco](imgPgit/ftFatec.jpg)
#### Projeto proposto pelo professor Flavio na Fatec Osasco
###### Deve-se realizar produção do sistema de uma urna eletrônica.
![urna eletrônica](imgPgit/urna.jpg)

------------------------------------------------------------------
## Linguagem:
- Python
## Requisito de software:
- Python3 em diante
## Banco de Dados:
- sqlite3
## Paradigmas de programação:
- Orientado á objeto
- Procedural
-------------------------------------------------------------------
## Documentação 

### Documentação do sistema
Ao iniciar o programa, é pedido o nome e senha do Adiministrador do sistema.
O nome de usuario Administrador é "root" e a senha é "123".
A com a permição de usuario Adiministrador, você podera cadastrar um Secretario, ver os Secretarios cadstrados, recuperar a senha de algum Secretario e se logar como Secretario.
Ao se logar como Secretario pode-se cadastrar Presidentes, Mesarios ou Candidatos, pode-se também mostrar destes os que estão cadastrados e se logar como Presidente.
Como Presidente é possivel limpar os dados do banco para iniciar a votação, mostrar os eleitores, fechar a eleição e computar votos, e se cadastrar como Mesario.
Como Mesario pode-se liberar a votação para os eleitores e voltar para o nivel presidente.
Os eleitores precisam digitar o seu CPF, seu nome e depois da demonstração dos candidatos cadstrados no sistema, pergunta-se em quem se deseja votar e depois disso cadstra-se o eleitor no sistema.

### Documentação das classes
###### os metodos que não estão especificados não passa-se atributos.
##### Métodos da classe administrador:
- menu: Mostra o menu de administrador.
- mostraSecretarios: Mostra os secretarios cadastrados no banco.
- inserirSecretario: insere um novo secretario no banco. Passa como atributo nome do secretario e a senha.
- recuperaSenha: Pede o nome e mostra a senha do usuario cadstrado no banco. Passa como atributo nome do secretario.
- loginSecretario: Loga como secretario. Passa como atributo nome e senha do usuario.
##### Métodos da classe secretario:
- menu: Mostra o menu de secretario.
- inserirPessoa: Serve tanto para inserir um Mesario quanto um Presidente, pois pede o serviço que será realizado pelo novo usuario cadstrado. Passa como atributo o nome, senha e serviço do usuario a ser cadastrado.
- inserirCandiato: Serve para inserir um candidato para ser votado, pede o numero que será oque os eleitores irão votar.Passa como atributo o numero a ser votado, nome e função que esta se elegendo.
- mostrarMesariosPresidentes: Serve para mostrar os mesarios e presidentes cadastrados.
- mostrarCandidatos: mostra os candidatos cadastrados no sistema.
- loginPresidente: Loga como Presidente. Passa como atributo o nome e senha para o presidente.
##### Métodos da classe presidente:
- menu: Mostra o menu para presidente.
- inicioVotacao: Limpa os votos atuais e inicia a votação
- loginMesario: Loga como Mesario. Passa como atributo o nome e senha para o mesario.
- computarVotos: Computa os votos nos candidatos.
- mostarEleitores: mostra os Eleitores que votaram.
##### Métodos da classe mesario:
- menu: Mostra o menu para mesario.
- inserirEleitor: Insere o eleitor no banco de dados Passa como atributo o cpf, nome e voto do eleitor.

--------------------------------------------------------------------------------------------------------

## Sobre os arquivos

- urna.py --> Contem as classes, atributos, métodos e tabelas do banco de dados (Orientado á objeto)
- main.py --> É o arquivo que chama os métodos das classes no programa (Procedural)
