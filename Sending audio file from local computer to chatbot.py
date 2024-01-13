import requests
import time

base_url = "" # insert the bot url
my_file =open("",'rb') #insert the path of the audio file

parameters = {
    "chat_id": "", #insert chat id
    "caption" : "Here is a your photo"
        }

files={
    "audio" :my_file
}

resp = requests.post(base_url, data=parameters,files=files)
print(resp.text)
