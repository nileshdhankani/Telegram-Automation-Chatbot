import requests
import pandas as pd


url=""

data = pd.read_csv(url, sep="\t")


base_url= ""

def read_message(offset):

  parameters = {
      "offset" : offset
  }
  resp=requests.get(base_url+"/getUpdates",data=parameters)
  data=resp.json()

  print(data)

  for result in data['result']:
    if "text" in result["message"]:
      send_msg(result["message"]["text"])

  if data["result"]:
    return data["result"][-1]["update_id"]+1

def auto_answer(message):
  answer=df.loc[df['Question'].str.lower()==message.lower()]

  if not answer.empty:
    answer=answer.iloc[0]['Answer']
    return answer
  else:
    return "Sorry i could not understand you!! I am still learning and try to get better in answering."


def send_msg(message):

  answer=auto_answer(message)
  parameters = {
      "chat_id": " ",
      "text": answer
  }

  resp = requests.get(base_url + "/sendMessage", data=parameters)
  print(resp.text)

offset=0
while True:
  offset=read_message(offset)