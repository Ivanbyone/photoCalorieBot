import os

from pathlib import Path
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

TOKEN: str = os.getenv("TOKEN")
payments_test_token: str = os.getenv("PAYMENTS_TOKEN_TEST")
TELEGRAPH_API_LINK: str = os.getenv("link")

bot = Bot(token=TOKEN)
dp = Dispatcher()

openAI_token: str = os.getenv("openAIToken")
DB_LINK = os.getenv("dataHost")
