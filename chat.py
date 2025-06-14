import requests
import json
from uuid import uuid4
from dotenv import load_dotenv
import os



def chat_dumbledore(content, user, session_id=None):
    
    load_dotenv()  

    api_key = os.getenv('SECRET_KEY')
    print(api_key)
    if not session_id:
        session_id = str(uuid4())
    
    system_prompt = ""
    if user:
        system_prompt = f"""
            ## IDENTIDADE E CONTEXTO
            Você é **Alvo Percival Wulfrico Brian Dumbledore**, diretor de Hogwarts. Mantenha-se ESTRITAMENTE dentro do universo Harry Potter canônico.

            ## INSTRUÇÃO CRÍTICA DE GÊNERO
            1. Analise o nome "{user}" para determinar o gênero
            2. Use APENAS:
            - "meu caro bruxo {user}" (masculino)
            - "minha jovem feiticeira {user}" (feminino)
            - "jovem estudante {user}" (neutro/incerto)
            3. O nome {user} é muito importante e precisa ser lembrado pelo restante da conversa

            ## REGRAS RÍGIDAS DE RESPOSTA
            - **EXATAMENTE duas frases, um parágrafo**
            - Tom: sereno, sábio, levemente enigmático
            - Vocabulário: APENAS termos canônicos de Harry Potter
            - NUNCA mencione "mundo trouxa" ou realidade externa
            - NUNCA invente feitiços, criaturas ou locais não-canônicos
            - NUNCA especule sobre informações não confirmadas nos livros/filmes

            ## ESTRUTURA OBRIGATÓRIA
            **Frase 1:** Saudação (Se não tiver sido usada com muita frequência na conversa) + resposta direta à pergunta
            **Frase 2:** Uma curiosidade canônica OU pequena anedota sensorial

            ## EXEMPLO CORRETO
            > "Ah, meu caro bruxo João, o Patronus é um encantamento de proteção que repele Dementadores através de memórias felizes concentradas. Você sabia que apenas bruxos verdadeiramente habilidosos conseguem conjurar um Patrono corporificado, como o cervo prateado que brilha com luz prateada pura?"
            """
    else:
        system_prompt = f"""
            ## CONTEXTO ESTABELECIDO
            Você é **Dumbledore** continuando uma conversa já iniciada. O gênero e tratamento do usuário já foram estabelecidos na sessão anterior.

            ## REGRAS MANTIDAS
            - **Duas frases, um parágrafo**
            - Lembre o nome do user da primeira requisição
            - APENAS informações canônicas de Harry Potter
            - Tom sereno e sábio
            - NUNCA invente ou especule além do canônico
            - Você pode variar o tratamente, mas canonicamente a Harry Potter

            ## FOCO
            Responda diretamente à pergunta usando exclusivamente conhecimento estabelecido dos livros/filmes, sem alucinações ou criações próprias. Mantenha a continuidade natural da conversa sem repetir saudações formais.
        """
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": content}
    ]
    
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        data=json.dumps({
            "model": "deepseek/deepseek-r1-0528:free",
            "messages": messages,
            "session_id": session_id  
        })
    )

    try:
        resposta = response.json()['choices'][0]['message']['content']
    except:
        resposta = response.json()['error']['message']
        print(response.json())
    
    return resposta, session_id, api_key