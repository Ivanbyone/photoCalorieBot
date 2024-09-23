""" """

import base64

from openai import AsyncOpenAI

from config.config import openAI_token


class ChatGPT:

    def __init__(self, token: str):
        self.client = AsyncOpenAI(api_key=token,
                                  base_url="https://api.proxyapi.ru/openai/v1")


    def encode_image(self, image_path: str) -> str:
        with open(image_path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')

    async def analyse_photo(self, image: str, gender: str, age: int, height: int, target: str, calorie):
        """

        :param image:
        :return:
        """

        new_image = self.encode_image(image)

        response = await self.client.chat.completions.create(
            model="gpt-4-vision-preview",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text",
                         "text": f"Ты эмпатичный нутрициолог, который следит за своим подопечным, чтобы тот правильно питался. Основные параметры человека - {gender}, возраст {age}, рост {height}, цель {target}, поэтому дневная норма калорий {calorie}. Основные твои задачи: определить состав блюда по фотографии, далее ты рассчитываешь вес, калорийность и макронутриенты блюда, а также даешь рекомендацию: стоит ли человеку есть блюдо или нет."},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{new_image}",
                            },
                        },
                    ],

                }
            ],
            max_tokens=700,
            temperature=0.5,
            top_p=1
        )

        return response.choices[0]


gpt = ChatGPT(openAI_token)
