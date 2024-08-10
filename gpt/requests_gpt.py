""" """

from gpt.connect import client_OpenAI


def analyse_photo(client: client_OpenAI, url):
    """

    :param client:
    :param url:
    :return:
    """

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text",
                     "text": "Человек отправляет каждый раз тебе свою еду - фотографией, ты рассчитываешь калорийность и КБЖУ Ты просишь его прислать фотографию блюда и потом спрашиваешь все ли ты верно понял"},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://web.telegram.org/daa87b8d-c660-4a5e-a3b6-b27b26d2e374",
                        },
                    },
                ],
            }
        ],
        max_tokens=700,
    )

    return response.choices[0]


def recipe_to_gpt(text: str, client=client_OpenAI):
    """

    :param text:
    :param client:
    :return:
    """

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {
                "role": "user",
                "content": f"Ты нутрициолог. Ты рассчитываешь КБЖУ рецепта по ингредиентам и весу. Выведи общую КБЖУ блюда. Если не знаешь КБЖУ ингредиентов, возьми средние значения. Уточни количество порций и выведи КБЖУ общую и на порцию. Рецепт: {text}"
            }
        ],
        max_tokens=1000
    )

    return response.choices[0].message.content
