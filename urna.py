import sqlite3
class administrador:
    def __init__(self, MASTER_PASSWORD, nomeAdm):
        self.MASTER_PASSWORD = MASTER_PASSWORD
        self.nomeAdm = nomeAdm
    conex = sqlite3.connect('logins2.db')
    cursor = conex.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_secretario(
        nomeUsuario text not null,
        password text not null
    );  ''')
    def barra(self, n=40, caractere='*'):
        print (caractere*n)

    def menu(self):
        self.barra()
        print("$ i -> Cadastrar o secretario ")
        print("$ r -> Recuperar senha do secretario")
        print("$ l -> listar secretarios cadastrados")
        print("$ s -> sair do sistema")
        self.barra()

    def mostraSecretarios(self):
        self.cursor.execute('''
            SELECT * FROM tbl_secretario
        ''')
        for i in self.cursor.fetchall():
            print (i)

    def inserirSecretario(self,nomeUsuario, password):
        self.nomeUsuario = nomeUsuario
        self.password = password
        self.cursor.execute(f'''
            INSERT INTO tbl_secretario VALUES 
            ('{self.nomeUsuario}','{self.password}') 
        ''')
        self.conex.commit()

    def recuperaSenha(self, nomeUsuario):
        self.nomeUsuario = nomeUsuario
        self.cursor.execute(f'''
            select * from tbl_secretario
            where nomeUsuario = '{self.nomeUsuario}'
        ''')
        if self.cursor.rowcount == 0 :
            print('nenhum usuario com essas especificações')
        else:
            for nomeUsuario in self.cursor.fetchall():
                print(nomeUsuario)

class secretario:
    def __init__(self,senhaSecretario, nomeSecretario):
        self.senhaSecretario = senhaSecretario
        self.nomeSecretario = nomeSecretario

    conex = sqlite3.connect('logins2.db')
    cursor = conex.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_pessoa(
        service text not null,
        nomeUsuario text not null,
        password text not null
    );  ''')
    def barra(self, n=40, caractere='*'):
        print (caractere*n)

    def loginSecretario(self):
        login = self.cursor.execute(f'''
        SELECT * FROM tbl_secretario where nomeUsuario = clara
        and password = 123
        ''')
        print(login)
    def menu(self):
        self.barra()
        print("$ P -> Cadastrar Presidente ")
        print("$ M -> Cadastrar Mesario ")
        print("$ C -> Cadastrar Candidato ")
        print("$ E -> Cadastrar Eleitor ")
        print("$ s -> sair do sistema")
        self.barra()

    def inserirPessoa(self,service, nomeUsuario, password):
        self.service = service
        self.nomeUsuario = nomeUsuario
        self.password = password
        self.cursor.execute(f'''
            INSERT INTO tbl_pessoa VALUES 
            ('{self.service}','{self.nomeUsuario}','{self.password}') 
        ''')
        self.conex.commit()
