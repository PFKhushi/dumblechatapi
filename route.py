from flask import request, jsonify
from main import app
from chat import chat_dumbledore



@app.route("/", methods=['POST'])
def homepage():
    
    dados = request.get_json()
    nome = None
    id = None
    content = None
    if 'nome' in dados:
        nome = dados['nome']
    if 'session' in dados: 
        id = dados['session_id'] 
    if 'content' in dados:
        content = dados['content']
    
    if nome and content:
        resposta, session = chat_dumbledore(
            content=content,
            user=nome
            )
        return {"resposta": resposta, "session_id": session, "key": key, "outro": [id, nome, content]}
    
    elif id and content:
        resposta, session, key = chat_dumbledore(
            content=content,
            session_id=id
            )
        return {"resposta": resposta, "session_id": session, "key": key, "outro": [id, nome, content]}
    
    else:
        return {"erro": "Faltam informações.", "fields": [content, session, nome]}        

