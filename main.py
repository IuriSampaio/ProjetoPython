from urna import *

adm = administrador('123456','iuri')
nome = input('digite o nome do adiminstrador: ')
senha = input("insira uma senha: ")
if senha != adm.MASTER_PASSWORD and nome != adm.nomeAdm:
    print("SENHA INVALIDA")
    exit()
else:
    while True:
        adm.menu()
        op = input("oque deseja fazer?")
        if op not in ['1','2','3','4','99']:
            print('não foi cadastrado nenhuma ação para essa key')
            continue
        if op == '1':
            nomeS = input('qual é do secretário? ')
            senhaS = input('digite uma senha? ')
            adm.inserirSecretario(nomeS,senhaS)
        if op == '3':
            adm.mostraSecretarios()
        if op == '2':
            nomeUsuario = input('qual é o seu nome? ')
            adm.recuperaSenha(nomeUsuario)
        if op == '4':
            sec = input('Digite o nome:')
            senha = input('Digite a senha:')
            if(adm.loginSecretario(sec,senha)):
                sec = secretario(senha, sec)
                while True:
                    sec.menu()
                    op = input("oque você deseja fazer?")
                    if op == '1':
                        cargo = input("digite oque essa pessoa vai fazer: ")
                        nome = input("digite o nome: ")
                        senha = input("digite a senha: ")
                        sec.inserirPessoa(cargo,nome,senha)
                        
                    if op == '2':
                        numero = input("digite o numero do candidato")
                        nome = input("digite o nome do candidato")
                        funcao = input("digite a função para qual o candidato se elegeu")
                        sec.inserirCandiato(numero,nome,funcao)
                    if op == '3':
                        cpf=input("digite seu cpf: ")
                        nome=input("digite seu nome: ")
                        print("============OPÇÕES DE VOTO===========")
                        sec.mostrarCandidatos()
                        voto=input("em quem vc vai votar? ")
                        sec.inserirEleitor(cpf,nome,voto)
                    if op == '4':
                        sec.mostrarMesariosPresidentes()
                    if op == '5':
                        sec.mostrarCandidatos()
                    if op == '6':
                        sec.mostarEleitores()
                    if op == '7':
                        sec.computarVotos()
                    if op == '99':
                        break                      
            else:
                print("não existe esse secretario")
                continue

        if op == '99':
            break
            


    