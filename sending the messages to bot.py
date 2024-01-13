import requests
import time

base_url = "" #insert your bot url

jokes = ["I invented a new world", "joke1", "joke2", "joke3", "joke4"]

for joke in jokes:
    time.sleep(10)
    parameters = {
        "chat_id": "",  #insert the chat id by reading the messages
        "text": joke
    }

    resp = requests.post(base_url, data=parameters)
    print(resp.text)
