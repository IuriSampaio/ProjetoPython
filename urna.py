import sqlite3
class administrador:
    conex = sqlite3.connect('logins2.db')
    cursor = conex.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_secretario(
        nomeUsuario text not null,
        password text not null
    );  ''')
    def __init__(self, MASTER_PASSWORD, nomeAdm):
        self.MASTER_PASSWORD = MASTER_PASSWORD
        self.nomeAdm = nomeAdm

    def barra(self, n=40, caractere='*'):
        print (caractere*n)

    def menu(self):
        self.barra()
        print("$ 1 -> Cadastrar o secretario ")
        print("$ 2 -> Recuperar senha do secretario")
        print("$ 3 -> listar secretarios cadastrados")
        print("$ 4 -> logar como secretario")
        print("$ 99 -> sair do sistema")
        self.barra()

    def mostraSecretarios(self):
        self.cursor.execute('''
            SELECT * FROM tbl_secretario
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            print (f'Nome: {i[0]} \nSenha: {i[1]} ')
        input("press enter to continue...")

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
                print(f'A senha para {nomeUsuario[0]} é {nomeUsuario[1]}')
        input("pressione qualquer tecla para continuar ...")

    def loginSecretario(self,nomeSecretario, senhaSecretario):
        self.nome = nomeSecretario
        self.senha = senhaSecretario
        self.cursor.execute(f'''
        SELECT * FROM tbl_secretario 
        where nomeUsuario = '{self.nome}'
        and password = '{self.senha}'
        ''')
        if self.cursor.rowcount == 0 :
            print('Esse usuario não está cadastrado !!')
            return False
        else:
            print(f'Olá {self.nome}')
            return True

class secretario:
    conex = sqlite3.connect('loginUsers.db')
    cursor = conex.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_pessoa(
        service text not null,
        nomeUsuario text not null,
        password text not null
    );
     ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_candidato2(
        idCandidato int not null primary key unique,
        nomeCandidato text not null,
        funcaoCandidatura text not null
    );
     ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tbl_eleitor(
        idEleitor int not null primary key unique,
        nomeEleitor text not null,
        idVoto int not null
    );
     ''')

    def __init__(self,senhaSecretario, nomeSecretario):
        self.senhaSecretario = senhaSecretario
        self.nomeSecretario = nomeSecretario

    barra = lambda self, n=40, caractere='*':print(caractere*n) 

    def menu(self):
        self.barra()
        print("$ 1 -> Cadastrar Presidente ou Mesario")
        print("$ 2 -> Cadastrar Candidato")
        print("$ 3 -> Cadastrar Eleitor")
        print("$ 4 -> Mostar mesarios e presidentes do TRE")
        print("$ 5 -> Mostar Candidatos")
        print("$ 6 -> Mostrar eleitores e votos")
        print("$ 7 -> Computar votos")
        print("$ 99 -> sair do sistema")
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

    def inserirCandiato(self, idCandidato, nomeCandidato,funcaoCandidatura ):
        self.idCandidato = idCandidato
        self.nomeCandidato = nomeCandidato
        self.funcao = funcaoCandidatura
        self.cursor.execute(f'''
            INSERT INTO tbl_candidato2 VALUES
            ('{self.idCandidato}','{self.nomeCandidato}','{self.funcao}')
        ''')
        self.conex.commit()

    def mostrarCandidatos(self):
        self.cursor.execute('''
            SELECT * FROM tbl_candidato2
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            print (f'Código para voto: {i[0]} \nNome: {i[1]}\nFunção: {i[2]} ')
        input("press enter to continue...")

    def inserirEleitor(self, cpf, nomeEleitor, votoEleitor):
        self.cpf = cpf
        self.nomeEleitor = nomeEleitor
        self.votoEleitor = votoEleitor
        self.cursor.execute(f'''
            INSERT INTO tbl_eleitor VALUES
            ('{self.cpf}','{self.nomeEleitor}','{self.votoEleitor}')
            ''')
        self.conex.commit()

    def mostrarMesariosPresidentes(self):
        self.cursor.execute('''
            SELECT * FROM tbl_pessoa
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            print (f'Serviço: {i[0]} \nNome: {i[1]} \nSenha: {i[2]} ')
        input("press enter to continue...")

    def mostarEleitores(self):
        self.cursor.execute('''
            SELECT * FROM tbl_eleitor
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            self.cursor.execute(f'''
            SELECT * FROM tbl_candidato2 where idCandidato = {i[2]} 
            ''')
            for j in self.cursor.fetchall():
                print (f'CPF: {i[0]} \nNome: {i[1]} \nVotou em: {j[1]} para {j[2]} ')
        input("press enter to continue...")

    def computarVotos(self):
        self.cursor.execute('''
        SELECT idVoto from tbl_eleitor
        ''')
        for i in self.cursor.fetchall():
            self.cursor.execute(f'''
            SELECT * from tbl_candidato2          
            ''')
            for j in self.cursor.fetchall():
                #print(j[0], i[0])
                if(j[0] == i[0]):
                    print(i[0])
        
