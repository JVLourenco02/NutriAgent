import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv


load_dotenv()

def conectar_db():
   
    try:
        conexao = mysql.connector.connect(
            host="localhost",
            user="root",          
            password="root",          
            database="nutriagent" 
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados MySQL: {e}")
        return None

def salvar_usuario(nome, idade, sexo, peso, altura, nivel_atividade):
    """Insere um novo usuário na tabela 'usuario' e retorna o ID gerado."""
    conexao = conectar_db()
    if conexao is None:
        return None
    
    try:
        cursor = conexao.cursor()
        query = """
            INSERT INTO usuario (nome, idade, sexo, peso_atual, altura, nivel_atividade) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        valores = (nome, idade, sexo, peso, altura, nivel_atividade)
        
        cursor.execute(query, valores)
        conexao.commit()
        
        # Pega o ID do usuário que acabou de ser inserido
        id_usuario = cursor.lastrowid
        return id_usuario
        
    except Error as e:
        print(f"Erro ao inserir usuário: {e}")
        return None
        
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()