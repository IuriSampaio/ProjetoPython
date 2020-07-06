from urna import *
while True:
    main = menuPrincipal()
    main.menu()
    op = input("oque deseja fazer?")
    if op not in ['1','2','3','4','99']:
        print("opção não cadastrada")
    if op == '1':
        adm = administrador('123','root')
        nome = input('digite o nome do adiminstrador: ')
        senha = input("insira uma senha: ")
        if senha != adm.MASTER_PASSWORD or nome != adm.nomeAdm:
            print("SENHA INVALIDA OU NOME INVALIDO")
            exit()
        else:
            while True:
                adm.menu()
                op = input("oque deseja fazer?")
                if op not in ['1','2','3','5']:
                    print('não foi cadastrado nenhuma ação para essa key')
                    continue
                if op == '1':
                    nomeS = input('qual é do secretário? ')
                    senhaS = input('digite uma senha? ')
                    adm.inserirSecretario(nomeS,senhaS)
                if op == '2':
                    adm.mostraSecretarios()
                if op == '3':
                    nomeUsuario = input('qual é o seu nome? ')
                    adm.recuperaSenha(nomeUsuario)
                if op == '5':
                    break
    if op == '2':
        sec = input('Digite o nome:')    
        senha = input('Digite a senha:')
        if(main.loginSecretario(sec,senha)):
            sec = secretario()
            while True:
                sec.menu()
                op = input("oque você deseja fazer?")
                if op not in ['1','2','3','4','5']:
                    print('não foi cadastrado nenhuma ação para essa key')
                    continue
                if op == '1':
                    cargo = input("digite oque essa pessoa vai fazer: ")
                    nome = input("digite o nome: ")
                    senha = input("digite a senha: ")
                    sec.inserirPessoa(cargo.lower(),nome,senha)
                if op == '2':
                    numero = input("digite o numero do candidato")
                    if not numero.isdigit():
                        continuar = True
                        while continuar:
                            print('APENAS NUMEROS')
                            numero = input("digite o numero do candidato")
                            if numero.isdigit():
                                continuar = False
                            else:
                                continue            
                    nome = input("digite o nome do candidato")
                    funcao = input("digite a função para qual o candidato se elegeu")
                    sec.inserirCandiato(numero,nome,funcao)
                if op == '3':
                    sec.mostrarMesariosPresidentes()
                if op == '4':
                    sec.mostrarCandidatos()
                if op == '5':
                    break
    if op == '3':
        nomeP = input('digite o nome do presidente: ')
        senhaP = input('digite a senha: ')
        if(main.loginPresidente(nomeP,senhaP)):
            pres = presidente(nomeP,senhaP)
            while True:
                pres.menu()
                ops = input("oque você deseja fazer ?")         
                if ops not in ['1','2','3','5']:
                    print("opção não cadastrada")
                    continue
                if ops == '1':
                    pres.inicioVotacao()
                if ops == '2':
                    pres.mostarEleitores()
                if ops == '3':
                    pres.computarVotos()
                    input("pressione enter para sair")
                    break
                if ops == '5':
                    break
                else:
                    print('esse cara não ta cadatrado') 
                    continue
                                      
        else:
            print("não existe esse secretario")
            continue
    if op == '4':
        nomeM = input('digite p nome do mesario: ')
        senhaM = input('digite a senha: ')
        if(main.loginMesario(nomeM,senhaM)):
            mes = mesario(nomeM,senhaM)
            while True:
                mes.menu()
                op = input("oque você deseja fazer?")
                if op not in ['1','2']:
                    print('não foi cadastrado nenhuma ação para essa key')
                    continue
                if op == '1':
                    cpf=input("digite seu cpf: ")
                    nome=input("digite seu nome: ")
                    print("============OPÇÕES DE VOTO===========")
                    sec =secretario()
                    sec.mostrarCandidatos()
                    voto=input("em quem vc vai votar? ")
                    mes.inserirEleitor(cpf,nome,voto)
                if op =='2':
                    break    
        else:
            print('mesario não cadastrado')
            continue                            
    if op == '99':
        break
            