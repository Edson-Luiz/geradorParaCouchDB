import random
import string
import json
import requests

username = 'username'
password = 'password'

# Lista de nomes
nomes = ['João', 'Maria', 'Pedro', 'Ana', 'José', 'Mariana', 'Carlos', 'Laura']

# Lista de sobrenomes
sobrenomes = ['Silva', 'Santos', 'Oliveira', 'Pereira', 'Rodrigues', 'Ferreira', 'Almeida']

# Função para gerar um nome aleatório
def gerar_nome():
    nome = random.choice(nomes)
    sobrenome = random.choice(sobrenomes)
    return f'{nome} {sobrenome}'

# Função para gerar uma rede social aleatória
def gerar_rede_social():
    redes_sociais = ['Facebook', 'Twitter', 'Instagram']
    return random.choice(redes_sociais)

# Função para gerar um número aleatório de seguidores
def gerar_seguidores():
    return random.randint(0, 10000)

# Função para gerar um post aleatório
def gerar_post():
    posts = [
        {"conteudo": "Olá, pessoal! Estou animado para começar essa nova rede social!"},
        {"conteudo": "Que dia lindo! #blessed"},
        {"conteudo": "Gostaria de saber se alguém tem recomendações de séries para assistir."},
        {"conteudo": "Daora dms"},
        {"conteudo": "kkkkkkkkk"},
        {"conteudo": "Nunca pensei que faria isso."}  
    ]
    return random.choice(posts)

# URL do CouchDB
couchdb_url = 'http://127.0.0.1:5984/'

# Número de documentos a serem gerados
num_documentos = 1000

url_banco = f'{couchdb_url}/redes_sociais_db/'

# Loop para gerar e inserir os documentos
for i in range(1, num_documentos + 1):
    documento = {
        "_id": str(i),
        "nome": gerar_nome(),
        "posts": gerar_post(),
        "rede_social": gerar_rede_social(),
        "seguidores": gerar_seguidores()  
    }

    # Inserção do documento no CouchDB
    response = requests.post(url_banco, auth=(username, password), json=documento)

    if response.status_code == 201:
        print(f"Documento {i} inserido com sucesso!")
    else:
        print(f"Erro ao inserir documento {i}: {response.text}")
