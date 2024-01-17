import tornado.httpclient
import json

url = "http://localhost:8888/?name=Vidoosh&age=20"

http_client = tornado.httpclient.HTTPClient()

try:
    response = http_client.fetch(url, method="GET")
    print("GET Response:", response.body.decode())

except tornado.httpclient.HTTPError as e:
    print(f"Error: {e}")

finally:
    http_client.close()

post_url = "http://localhost:8888/"

post_data = {
    "name" : "Vidoosh",
    "age" : "70",
    "industry" : "publiccvb",
    "salary" : "50",
    "city" : "Chennai"    
}

http_client = tornado.httpclient.HTTPClient()

try:
    request = tornado.httpclient.HTTPRequest(post_url, method="POST", body=json.dumps(post_data), headers={'Content-type': 'application/json'})
    response = http_client.fetch(request)
    print("POST Response:", json.loads(response.body.decode()))

except tornado.httpclient.HTTPError as e:
    print(f"Error: {e}")

finally:
    http_client.close()