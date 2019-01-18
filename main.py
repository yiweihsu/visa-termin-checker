import requests

url = 'https://formular.berlin.de/xima-forms-29/get/14963116144270000'

session_requests = requests.Session()
print(session_requests.cookies.get_dict())

r = session_requests.get(url)
print(session_requests.cookies.get_dict())