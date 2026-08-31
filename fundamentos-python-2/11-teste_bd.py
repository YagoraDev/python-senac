import pymysql

DB_CONFIG = {
    'host': 'localhost', # Endereço do servidor MySQL
    'user': 'root',      # Usuário do banco de dados
    'password': '',      # Senha do usuário do banco de dados
    'database': 'bdclientes', # Nome do banco de dados
    'charset': 'utf8mb4', # Conjunto de caracteres a ser usado na conexão
    'cursorclass': pymysql.cursors.Cursor, # Tipo de cursor a ser usado na conexão
    'autocommit': False # Ativa ou desativa o autocommit (True para ativar, False para desativar)
}

# Função para conectar ao banco de dados
def conectar():
    return pymysql.connect(**DB_CONFIG) # Cria uma conexão com o banco de dados usando as configurações definidas em DB_CONFIG

def testar_conexao():
    try:
        conexao = conectar() # Tenta conectar ao banco de dados
        print("Conexão bem-sucedida!") # Se a conexão for bem-sucedida, imprime uma mensagem de sucesso
    except pymysql.MySQLError as e: # Captura erros relacionados ao MySQL
        print(f"Erro ao conectar ao banco de dados: {e}") # Imprime a mensagem de erro
    finally:
        if 'conexao' in locals() and conexao.open: # Verifica se a conexão foi criada e está aberta
            conexao.close() # Fecha a conexão com o banco de dados
            print("Conexão encerrada.") # Imprime uma mensagem indicando que a conexão foi encerrada

if __name__ == "__main__":
    testar_conexao() # Chama a função para testar a conexão com o banco de dados