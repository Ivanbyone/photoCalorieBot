import os

from pathlib import Path
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

token: str = os.getenv("TOKEN")
payments_test_token: str = os.getenv("PAYMENTS_TOKEN_TEST")

bot = Bot(token=token)
dp = Dispatcher()
