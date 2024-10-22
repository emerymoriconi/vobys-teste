import requests
import mysql.connector
import os

# URL BASE DA API DO IBGE UTILIZADA NESSE TESTE
url_base = "https://servicodados.ibge.gov.br/api/v1/paises/"

# BUSCAR DADOS NA API
def buscar_da_api(codigo_pais):
    url = f"{url_base}{codigo_pais}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return f"Erro durante a busca: {resposta.status_code}"

# CONECTAR AO BANCO DE DADOS

def conectar_banco():
    return mysql.connector.connect( 
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# CRIAR TABELA
def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("CREATE TABLE paises (id INT AUTO_INCREMENT PRIMARY KEY, codigo VARCHAR(3), nome VARCHAR(100), area VARCHAR(100), regiao VARCHAR(100), sub_regiao VARCHAR(100))")

    cursor.close()
    conexao.close()

# CONEXÃO E INSERT 
def inserir_pais(codigo, nome, area, regiao, subregiao):
    conexao = conectar_banco()
    cursor = conexao.cursor()

    query = "INSERT INTO paises (codigo, nome, area, regiao, sub_regiao) VALUES (%s, %s, %s, %s, %s)"

    valores = (codigo, nome, area, regiao, subregiao)
    cursor.execute(query, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

# BUSCA NA API E INSERT
def buscar_e_inserir_pais(codigo_pais):
    url = f"{url_base}{codigo_pais}"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()[0]
        nome = dados['nome']['abreviado']
        area = dados.get('area', {}).get('total', None)
        regiao = dados['localizacao']['regiao']['nome']
        sub_regiao = dados['localizacao']['sub-regiao']['nome']
        
        # inserir os dados no banco de dados
        inserir_pais(codigo_pais, nome, area, regiao, sub_regiao)
        print(f"Dados do país {nome} inseridos com sucesso!")
    else:
        print(f"Erro ao buscar país: {resposta.status_code}")

# SELECT * 
def buscar_paises():
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM paises")
    paises = cursor.fetchall()

    if not paises:
        print("Nenhum país encontrado")
        return

    for pais in paises:
        print(f"ID: {pais[0]}, Código: {pais[1]}, Nome: {pais[2]}, Área: {pais[3]}, Região: {pais[4]}, Sub-região: {pais[5]}")

    cursor.close()
    conn.close()

# DELETE
def deletar_pais(codigo_pais):
    conn = conectar_banco()
    cursor = conn.cursor()

    query = "DELETE FROM paises WHERE codigo = %s"
    valores = (codigo_pais,)
    cursor.execute(query, valores)
    
    conn.commit()
    print(f"País com código {codigo_pais} removido com sucesso!")
    
    cursor.close()
    conn.close()


