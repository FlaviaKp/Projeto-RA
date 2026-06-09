import sqlite3

def cadastra_db(cpf, nome, idade, problemas_saude):
    connection = sqlite3.connect("meu_banco.db") #criar o banco de dados/se ja existir o db, ele so conecta -->> database
    carlos = connection.cursor() #Carlos é o robo executa as funções dentro do banco de dados --> grava, le // connection.cursor -> pega a função de cursor(robo) do sqlite3

    carlos.execute(""" 
    CREATE TABLE IF NOT EXISTS clientes(
                cpf TEXT PRIMARY KEY NOT NULL,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                problemas_saude TEXT NOT NULL
    )
    """) #cria a tabela cliente se nao existir no banco de dados

    carlos.execute(
        "INSERT INTO clientes(cpf, nome, idade, problemas_saude) VALUES (?,?,?,?)",
        (cpf, nome, idade, problemas_saude)
    ) #insere  os dados do cliente no banco de dados

    connection.commit() #salva as alterações no db.
    connection.close() #fecha a conecção no db.

    return("Cadrastro concluido com sucesso!")

def editar_clientes(cpf, nome, idade, problemas_saude):
    connection = sqlite3.connect("meu_banco.db") 
    carlos = connection.cursor()

    dados = {
        "nome": nome,
        "idade": idade,
        "problemas_saude": problemas_saude
    }

    dados = {k: v for k, v in dados.items() if v != ""}

    campos = ", ".join(f"{k} = ?" for k in dados)
    valores = list(dados.values())
    valores.append(cpf)

    carlos.execute(f"UPDATE clientes SET {campos} WHERE cpf = ?", valores)

    print("\nCliente editado com sucesso!")

    connection.commit()
    connection.close

    return

def excluir_cliente(cpf):
    connection = sqlite3.connect("meu_banco.db") 
    carlos = connection.cursor()

    carlos.execute("DELETE FROM clientes WHERE cpf = ?", (cpf,))

    connection.commit()
    connection.close()

    print("\nCliente deletado com sucesso!")

    return

def listar_clientes(): 
    connection = sqlite3.connect("meu_banco.db") 
    carlos = connection.cursor()

    carlos.execute("SELECT cpf, nome, idade, problemas_saude FROM clientes")
    clientes = carlos.fetchall()
    connection.close
    print("Lista de clientes")
    print(f"\n {clientes}")
    
    return

