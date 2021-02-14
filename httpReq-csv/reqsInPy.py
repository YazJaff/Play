import requests
import json
#method='POST'
method='GET'
url='https://www.google.com'
#url='http://vthinkbeyondvm.com/getting-started-with-vcenter-server-rest-apis-using-python/'
#payload='Hello API world'
header={'content-type':'application/json'}
req=requests.request(method,url)
print(req.status_code)