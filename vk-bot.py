import vk_api
import time
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime
from config import TOKEN


session = vk_api.VkApi(token=TOKEN)
session_api = session.get_api()
longpoll = VkLongPoll(session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            print("Сообщение пришло в: " + str(event.datetime))
            print("Текст сообщения: " + str(event.text))

            response = event.text.lower()
            if event.from_user and not event.from_me:

                if response.find("привет") >= 0 or response.find("здраствуй") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет",
                            "sticker_id": 85009,
                            "random_id": 0,
                        },
                    )
                elif response.find("пока") >= 0 or response.find("до свидания") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "До скорой встречи",
                            "random_id": 0,
                        },
                    )
                elif response.find("как дел") >= 0 or response.find("как жизнь") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {"user_id": event.user_id, "message": "Хорошо", "random_id": 0},
                    )
                elif response.find("что делаешь") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {"user_id": event.user_id, "message": "нечего", "random_id": 0},
                    )
                elif response.find("как настроение") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {"user_id": event.user_id, "message": "Хорошо", "random_id": 0},
                    )
                elif response == "ку" or response == "куку":
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {"user_id": event.user_id, "message": "ку", "random_id": 0},
                    )
                elif response.find("ты бот") >= 0 or response.find("ботик ты") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "сам бот",
                            "random_id": 0,
                        },
                    )
                elif response.find("занят") >= 0 or response.find("мешаю") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "вохможно",
                            "random_id": 0,
                        },
                    )
                elif response.find("мне грустно") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {"user_id": event.user_id, "sticker_id": 84669, "random_id": 0},
                    )
                elif response.find("ава") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "photo487155786_457240854",
                            "random_id": 0,
                        },
                    )
                elif response.find("музыка") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "audio-2001836161_52836161",
                            "random_id": 0,
                        },
                    )
                elif response.find("сф") >= 0:
                    time.sleep(random.uniform(0.5, 3))
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "attachment": "video540473276_456239161",
                            "random_id": 0,
                        },
                    )
