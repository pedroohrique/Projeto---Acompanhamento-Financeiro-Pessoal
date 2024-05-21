import pyodbc


def database_connection(): #Instânciar uma função que receberá parametros de conexão com o banco de dados através das variáveis (server, database, user, password)
    server = 'DESKTOP-LV5SLNK\ADMIN' # -> Registra o valor do server que futuramente passaremos para uma variável de conexão chamada "connection"
    database = 'FINANCEIRO' # -> Registra o valor da respectiva base que futuramente passaremos para uma variável de conexão chamada "connection"
    user = 'Admin' # -> Registra o valor do usuário de conexão com o BD que futuramente passaremos para uma variável de conexão chamada "connection"
    password = '66tUa3ue' # -> Registra o valor da senha de conexão com o BD que futuramente passaremos para uma variável de conexão chamada "connection"


    # Após dados de conexão armazenados, devemos realizar a conexão de fato.
    # Para isso utilizaremos as palavras-chave "try" e "except" como tratamento de erro e excessão
    try:
        
        #Variváel que realiza a conexão com o BD concatenando o DRIVER da biblioteca "pyodbc" com os dados registrados nas variáveis da function "database_connection"
        connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + user + ';PWD=' + password)

        # Variável "cursor" resonsável por executar a conexão com o banco através da função nativa "cursor()"
        cursor = connection.cursor()
        print('Conexão estabelecidade com sucesso!')

        # Após concluído, a função retorna a conexão e a execução do cursor
        return connection, cursor

    # Caso haja um falha de conexão com o nosso banco, será exibido uma msg padrão + o erro ocorrido.
    except Exception as e:
        print('Erro ao se conectar com o banco de dados!', e)
        return e