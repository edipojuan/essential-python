import psycopg2

# --- 1. Defina os parâmetros da sua conexão ---
# Substitua com os dados do seu banco de dados PostgreSQL
db_params = {
    "host": "localhost",       # ou o IP/endereço do seu servidor
    "database": "mydb",
    "user": "user",
    "password": "password",
    "port": "5432"           # Opcional, 5432 é o padrão
}

conn = None  # Inicializa a variável de conexão como None
cursor = None # Inicializa a variável do cursor como None

try:
    # --- 2. Estabelecer a conexão ---
    print("Conectando ao banco de dados PostgreSQL...")
    conn = psycopg2.connect(**db_params)
    print("Conexão bem-sucedida!")

    # --- 3. Criar um cursor ---
    # O cursor é usado para executar comandos no banco de dados
    cursor = conn.cursor()

    # --- 4. Executar uma query SQL ---
    print("Executando query...")
    # Exemplo: selecionar a versão do PostgreSQL
    cursor.execute("SELECT version();")

   # --- 5. Buscar o resultado ---
    db_version = cursor.fetchone() # fetchone() para um único resultado
    print("Versão do PostgreSQL:", db_version)

except (Exception, psycopg2.Error) as error:
    print("Erro ao conectar ou buscar dados no PostgreSQL:", error)

finally:
    if cursor:
        cursor.close()
    if conn:
        conn.close()
        print("Conexão fechada.")