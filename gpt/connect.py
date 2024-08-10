""" """

from openai import OpenAI

from config.config import openAI_token

client_OpenAI = OpenAI(api_key=openAI_token,
                       base_url="https://api.proxyapi.ru/openai/v1")
