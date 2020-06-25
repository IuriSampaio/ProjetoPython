import sqlite3

MASTER_PASSWORD = "123456"

senha = input("insira uma senha: ")
if senha != MASTER_PASSWORD:
    print("SENHA INVALIDA")
    exit()

conex = sqlite3.connect('passwords.db')

cursor = conex.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS tbl_usuarios(
    service text not null,
    nomeUsuario text not null,
    password text not null
);
''')

def barra(n=40, caractere='$'):
    print (caractere*n)

def menu():
    barra()
    print("$ i -> para inserir uma nova senha")
    print("$ r -> Recuperar senha")
    print("$ l -> listar usuarios salvos")
    print("$ s -> sair")
    barra()




def mostraServices():
    cursor.execute('''
        SELECT * FROM tbl_usuarios
    ''')
    for service in cursor.fetchall():
        print (service)

def inserirSenha(service, nomeUsuario, password):
    cursor.execute(f'''
        INSERT INTO tbl_usuarios VALUES 
        ('{service}','{nomeUsuario}','{password}') 
    ''')
    conex.commit()

def recuperaSenha(service, nomeUsuario):
    cursor.execute(f'''
        select * from tbl_usuarios 
        where nomeUsuario = '{nomeUsuario}'
        and service = '{service}'

    ''')
    if cursor.rowcount == 0 :
        print('nenhum usuario com essas especificações')
    else:
        for nomeUsuario in cursor.fetchall():
            print(nomeUsuario)

while True:
    menu()
    op = input("oque deseja fazer?")
    if op not in ['i','r','l','s']:
        print('não foi cadastrado nenhuma ação para essa key')
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('qual é o seu serviço? ')
        nomeUsuario = input('qual é o seu nome? ')
        senha = input('digite uma senha? ')
        inserirSenha(service,nomeUsuario,senha)
    if op == 'l':
        mostraServices()
    if op == 'r':
        service = input('qual é o seu serviço? ')
        nomeUsuario = input('qual é o seu nome? ')
        recuperaSenha(service,nomeUsuario)
conex.close()