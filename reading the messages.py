import requests
base_url= "" #insert your bot usrl

parameters = {
    "offset" : "", #insert your offset
    "limit" : ""

}


resp=requests.get(base_url,data=parameters)
print(resp.text)