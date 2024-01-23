import tornado.httpclient
import json

url = "http://localhost:8888"

http_client = tornado.httpclient.HTTPClient()

post_data = {
    "name": "Vidoosh",
    "age": "70",
    "industry": "private",
    "salary": "50",
    "city": "Chennai",
}

try:
    request = tornado.httpclient.HTTPRequest(
        url,
        method="POST",
        body=json.dumps(post_data),
        headers={"Content-type": "application/json"},
    )
    response = http_client.fetch(request)
    c_id = response.body.decode()
    print("POST Response:", response.body.decode())

except tornado.httpclient.HTTPError as e:
    print(f"Error: {e}")

finally:
    http_client.close()

url = f"http://localhost:8888?c_id={c_id}"

http_client = tornado.httpclient.HTTPClient()

try:
    response = http_client.fetch(url, method="GET")
    print("GET Response:", json.loads(response.body.decode()))

except tornado.httpclient.HTTPError as e:
    print(f"Error: {e}")

finally:
    http_client.close()