import requests
from requests_ntlm import HttpNtlmAuth

auth = HttpNtlmAuth(domain+'\\'+username,password)

reponse = requests.get(url=auth_url,auth=auth,params=params)
if response.status_code == requests.codes.ok:
    result = response.json()
else:
  response.raise_for_status()
