import requests
import time

base_url = ""

urls = {
    "" # insert the bot url,
}
for url in urls:
  time.sleep(10)
  parameters = {
      "chat_id": "" #insert chat id,
      "photo": url,
      "caption" :'''''' #insert caption

  }
  resp = requests.post(base_url, data=parameters)
  print(resp.text)
