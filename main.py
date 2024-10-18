import requests
from openai import OpenAI
def call_chatgpt_api(api_key, prompt, model="gpt-4o-mini"):

    url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    data = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 150  # Limite de tokens na resposta, ajuste conforme necessário
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Erro {response.status_code}: {response.text}"

# Exemplo de uso
api_key = ""
prompt = "Me dê uma recomendação de livro de ficção científica."

resposta = call_chatgpt_api(api_key, prompt)
print(resposta)