# 🌎 API IBGE Countries

Um sistema simples de integração com a API de Países do IBGE que permite consultar e armazenar informações sobre países em um banco de dados MySQL.

## 📋 Sobre o Projeto

Este projeto realiza a integração com a API de Países do IBGE (Instituto Brasileiro de Geografia e Estatística) e oferece funcionalidades para:
- Consultar informações de países específicos
- Armazenar dados dos países em banco de dados MySQL
- Listar todos os países cadastrados
- Remover países do banco de dados

## 🛠️ Tecnologias Utilizadas

- Python 
- MySQL

## 🚀 Como Executar

### Pré-requisitos

1. Python 3.x instalado
2. MySQL Server instalado e rodando
3. Banco de dados 'api-connection' criado

### Configuração do Banco de Dados

1. Crie um banco de dados chamado 'api-connection'
2. O sistema criará automaticamente a tabela necessária

### Instalação

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

### Configuração

Ajuste as credenciais do banco de dados no arquivo `main.py`:
```python
def conectar_banco():
    return mysql.connector.connect( 
        host="127.0.0.1",
        user="seu_usuario",
        password="sua_senha",
        database="api-connection"
    )
```

### Execução

Execute o arquivo menu.py:
```bash
python menu.py
```

## 📱 Funcionalidades

O sistema oferece um menu interativo com as seguintes opções:

1. **Buscar país**: Consulta informações de um país específico na API do IBGE
2. **Inserir país**: Busca dados na API e salva no banco de dados
3. **Listar países**: Exibe todos os países salvos no banco de dados
4. **Deletar país**: Remove um país do banco de dados
5. **Sair**: Encerra o programa

## 🗃️ Estrutura do Banco de Dados

Tabela `paises`:
- id (INT, AUTO_INCREMENT, PRIMARY KEY)
- codigo (VARCHAR(3))
- nome (VARCHAR(100))
- area (VARCHAR(100))
- regiao (VARCHAR(100))
- sub_regiao (VARCHAR(100))

## 🌐 API Utilizada

API de Países do IBGE:
- URL Base: https://servicodados.ibge.gov.br/api/v1/paises/
- Documentação: [Link para documentação do IBGE]

## 📁 Estrutura do Projeto

```
├── main.py           # Funções principais e conexão com banco de dados
├── menu.py          # Interface do usuário
└── requirements.txt  # Dependências do projeto
```

## 👥 Autor

Émery Freitas Moriconi
