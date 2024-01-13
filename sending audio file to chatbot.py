import requests
import time

base_url = "" # insert the bot url

parameters = {
    "chat_id": "" #insert chat id,
    "audio": "", # insert audio file link

    "caption" : "Here is a your audio file"
        }

resp = requests.post(base_url, data=parameters)
print(resp.text)
