import requests
import time

base_url = "" # insert the bot url

parameters = {
    "chat_id": "", #insert chat id
    "photo": "", #insert the photo url
    "caption" : "Here is a your photo"
        }

resp = requests.post(base_url, data=parameters)
print(resp.text)
