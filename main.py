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
        if op not in ['i','r','l','s']:
            print('não foi cadastrado nenhuma ação para essa key')
            continue
        if op == 'i':
            nomeS = input('qual é do secretário? ')
            senhaS = input('digite uma senha? ')
            adm.inserirSecretario(nomeS,senhaS)
        if op == 'l':
            adm.mostraSecretarios()
        if op == 'r':
            nomeUsuario = input('qual é o seu nome? ')
            adm.recuperaSenha(nomeUsuario)
        if op == 's':
            # sec = input('Digite o nome:')
            # senha = input('Digite a senha:')
            secretario = secretario('clara','123') 
            secretario.loginSecretario()
               
            


    