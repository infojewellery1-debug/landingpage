import requests
url = "http://192.168.100.99:8090/httpclient.html"
print(requests.get(url, timeout=10).status_code)
