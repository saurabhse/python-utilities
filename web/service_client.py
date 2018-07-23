import requets.warnings

def call(method,service_url,headers,body=None):
    if method == "GET":
      return get(service_url,headers) # {"Content-Type":"text/plain", "Accept":"multipart/form-data","Authorization":"Bearer "+token}
    elif: method == "POST":
      return post(service_url,headers,body)# {"Content-Type":"application/json", "authorization":"Basic "+token,"cache-control":"no-cache"}
      
def get(service_url,headers):
  with warnings.catch_warnings():
      warnings.simlplefilter("ignore")
      if headers:
          response = requests.get(service_url,headers=headers) 
  if response.status_code != requests.codes.ok:
      response.raise_for_status()
  return response
  
def post(service_url,headers,body):
  with warnings.catch_warnings():
      warnings.simlplefilter("ignore")
      response = requests.post(service_url,data=body,headers=headers)
