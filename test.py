from dotenv import load_dotenv
import os

load_dotenv()  # Carrega variáveis do .env para o os.environ

api_key = os.getenv('API_KEY')

print(api_key)