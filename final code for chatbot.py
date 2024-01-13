import requests
import pandas as pd

url = ''

df = pd.read_csv(url, sep="\t")


base_url = ""



def read_msg(offset):

  parameters = {
      "offset" : offset
  }

  resp = requests.get(base_url + "/getUpdates", data = parameters)
  data = resp.json()

  print(data)

  for result in data["result"]:
    send_msg(result)

  if data["result"]:
    return data["result"][-1]["update_id"] + 1



def auto_answer(message):
  answer = df.loc[df['Question'].str.lower() == message.lower()]

  if not answer.empty:
      answer = answer.iloc[0]['Answer']
      return answer
  else:
      return "Sorry, this movie is not in our database. Please try the next keyword, or you can wait for our admins to reply."


def send_msg(message):
    if "message" in message and "text" in message["message"]:
        text = message["message"]["text"]
        message_id = message["message"]["message_id"]
        answer = auto_answer(text)

        parameters = {
            "chat_id": "",
            "text": answer,
            "reply_to_message_id": message_id
        }

        resp = requests.get(base_url + "/sendMessage", params=parameters)
        print(resp.text)
    else:
        print("Invalid message format:", message)


offset = 0

while True:
  offset = read_msg(offset)