import sqlite3

class menuPrincipal:
    

    barra = lambda self,n=40,caraca='*':print(caraca*n)

    def menu(self):
        self.barra()
        print("$ 1 -> Logar como Administrador")
        print("$ 2 -> Logar como Secretario")
        print("$ 3 -> Logar como Presidente")
        print("$ 4 -> Logar como Mesario")
        print("$ 99 -> Sair do sistema")
        self.barra()
    
    
    def loginSecretario(self,nomeSecretario, senhaSecretario):
        conex = sqlite3.connect('logins2.db')
        cursor = conex.cursor()
        self.nome = nomeSecretario
        self.senha = senhaSecretario
        cursor.execute(f'''
        SELECT * FROM tbl_secretario
        ''')
        for i in cursor.fetchall():
            if (i[0]==self.nome and i[1]==self.senha) :
                print(f'Olá {self.nome}')
                return True

    def loginPresidente(self, nome,senha):
        conex = sqlite3.connect('loginUsers.db')
        cursor = conex.cursor()
        self.nomeP=nome
        self.senhaP=senha
        cursor.execute('''
            SELECT * FROM tbl_pessoa
        ''')
        for i in cursor.fetchall():
            if (i[0].lower()=='presidente' and i[1]==self.nomeP and i[2]==self.senhaP):
                print(f'Ola {self.nomeP}')
                return True
        
        conex.commit()

    def loginMesario(self,nome,senha):
        conex = sqlite3.connect('loginUsers.db')
        cursor = conex.cursor()
        self.nomeM=nome
        self.senhaM=senha
        cursor.execute('''
            SELECT * FROM tbl_pessoa
        ''')
        for i in cursor.fetchall():
            if (i[0].lower()=='mesario' and i[1]==self.nomeM and i[2]==self.senhaM):
                print(f'Ola {self.nomeM}')
                return True
        
        conex.commit()


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

    barra = lambda self, n=40, caractere='*':print(caractere*n) 

    def menu(self):
        self.barra()
        print("$ 1 -> Cadastrar o secretario ")
        print("$ 2 -> listar secretarios cadastrados")
        print("$ 3 -> Recuperar senha do secretario")
        print("$ 5 -> Voltar para o menu principal")
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

    # def __init__(self,senhaSecretario, nomeSecretario):
    #     self.senhaSecretario = senhaSecretario
    #     self.nomeSecretario = nomeSecretario

    barra = lambda self, n=40, caractere='*':print(caractere*n) 

    def menu(self):
        self.barra()
        print("$ 1 -> Cadastrar Presidente ou Mesario")
        print("$ 2 -> Cadastrar Candidato")
        print("$ 3 -> Mostar mesarios e presidentes do TRE")
        print("$ 4 -> Mostar Candidatos")        
        print("$ 5 -> Voltar ao menu principal")
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

    def mostrarMesariosPresidentes(self):
        self.cursor.execute('''
            SELECT * FROM tbl_pessoa
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            print (f'Serviço: {i[0]} \nNome: {i[1]} \nSenha: {i[2]} ')
        input("press enter to continue...")
        self.conex.commit()

    
    def mostrarCandidatos(self):
        self.cursor.execute('''
            SELECT * FROM tbl_candidato2
        ''')
        for i in self.cursor.fetchall():
            self.barra()
            print (f'Código para voto: {i[0]} \nNome: {i[1]}\nFunção: {i[2]} ')
        input("press enter to continue...")

    

class presidente:
    conex = sqlite3.connect('loginUsers.db')
    cursor = conex.cursor()
    def __init__(self,nome,senha):
        self.senhaP=senha
        self.nomeP=nome

    barra = lambda self, n=40, caractere='*':print(caractere*n) 

    def menu(self):
        self.barra()
        print("$ 1 -> Iniciar Votação e limpar votos")
        print("$ 2 -> Mostrar Eleitores")
        print("$ 3 -> Fechar a votação e computar votos")
        print("$ 5 -> Voltar para o menu principal")
        self.barra()
    
    def inicioVotacao(self):
        self.cursor.execute('''
        delete from tbl_eleitor
        ''')
        if self.cursor.rowcount==0:
            print("não foi possivel limpar a votação")
        else:
            print("dados excluidos e votação iniciada")
        self.conex.commit()

    

    def computarVotos(self):
        votos=[]
        candidatos=[]
        n=[]
        self.cursor.execute('''
        SELECT idVoto from tbl_eleitor
        ''')
        for i in self.cursor.fetchall():
            votos.append(i[0])
        
        self.cursor.execute('''
        SELECT idCandidato from tbl_candidato2
        ''')
        for i in self.cursor.fetchall():
            candidatos.append(i[0])
        for i in range(votos.__len__()):
            n.append(list(filter(lambda x: x==candidatos[i] , votos)))
            if n[i]==[]:
                print(f'O candidato {candidatos[i]} não recebeu nenhum voto')
            else:
                print(f'o candidato {candidatos[i]} recebeu {n[i].__len__()} votos')
        self.conex.commit()

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
        self.conex.commit() 

class mesario:
    conex = sqlite3.connect('loginUsers.db')
    cursor = conex.cursor()
    def __init__(self,nome,senha):
        self.nome=nome
        self.senha=senha
    
    barra = lambda self, n=40, caractere='*':print(caractere*n) 
    
    def menu(self):
        self.barra()
        print("$ 1 -> Liberar votação para eleitores")
        print("$ 2 -> Voltar ao menu principal")
        self.barra()
    
    def inserirEleitor(self, cpf, nomeEleitor, votoEleitor):
        self.cpf = cpf
        self.nomeEleitor = nomeEleitor
        self.votoEleitor = votoEleitor
        self.cursor.execute(f'''
            INSERT INTO tbl_eleitor VALUES
            ('{self.cpf}','{self.nomeEleitor}','{self.votoEleitor}')
            ''')
        self.conex.commit()