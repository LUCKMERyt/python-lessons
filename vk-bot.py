import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from datetime import datetime

session = vk_api.VkApi(
    token="vk1.a.2ynYMv9EhvDWtQYQYnbiwpaadpTQCywUUYpw5Cca4-HBrxMh3sHZ9Ja3sbOoXer2LbI1s40Ear2cu-89Pd8rsjp3Jf6NmOA8uzTmv_RLs6rwkyfpCBRJN8jnulDoDvmRGQCpUmVpLuoPIQiX_tkTz_D34lii0FRHqIqTngBYoVnFmU6rOgkPZj4a5JMnVK9BEl-VPtMm0K0YJNyilPEm9A"
)
session_api = session.get_api()
longpoll = VkLongPoll(session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:

            print("Сообщение пришло в: " + str(event.datetime))
            print("Текст сообщения: " + str(event.text))

            response = event.text.lower()
            if event.from_user and not event.from_me:

                if response == "привет":
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "И тебе привет",
                            "random_id": 0,
                        },
                    )
                elif response == "пока":
                    session.method(
                        "messages.send",
                        {
                            "user_id": event.user_id,
                            "message": "До скорой встречи",
                            "random_id": 0,
                        },
                    )
