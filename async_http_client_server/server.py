import tornado.ioloop
import tornado.web
import json
import uuid


count = 0


class MainHandler(tornado.web.RequestHandler):
    all_responses = {}

    async def get(self):
        # client_id = str(uuid.uuid4())
        global count
        client_id = "C" + str(count)
        count = count + 1
        name = self.get_argument("name", default=None)
        age = self.get_argument("age", default=None)
        industry = self.get_argument("industry", default="private")
        salary = self.get_argument("salary", default="50000")
        city = self.get_argument("city", default="New York")

        if name is None or age is None:
            self.set_status(400)
            self.finish({"error": "Name and age are required."})
        else:
            response_data = {
                "client_id": client_id,
                "name": name,
                "age": age,
                "industry": industry,
                "salary": salary,
                "city": city,
            }
            self.save_response(client_id, response_data)
            self.finish(response_data)

    async def post(self):
        # client_id = str(uuid.uuid4())
        global count
        client_id = "C" + str(count)
        count = count + 1
        try:
            data = json.loads(self.request.body.decode())
            name = data.get("name", None)
            age = data.get("age", None)
            industry = data.get("industry", None)
            salary = data.get("salary", None)
            city = data.get("city", None)
            # name = self.get_body_argument("name", default=None)
            # age = self.get_body_argument("age", default=None)
            # industry = self.get_body_argument("industry", default="private")
            # salary = self.get_body_argument("salary", default="50000")
            # city = self.get_body_argument("city", default="New York")

            # print("Received data:", name, age, industry, salary, city)

            if name is None or age is None:
                self.set_status(400)
                self.finish({"error": "Name and age are required."})
            else:
                response_data = {
                    "client_id": client_id,
                    "name": name,
                    "age": age,
                    "industry": industry,
                    "salary": salary,
                    "city": city,
                }
                self.save_response(client_id, response_data)
                self.finish(response_data)

        except json.JSONDecodeError:
            self.set_status(400)
            self.finish({"Error": "Invalid json"})

    def save_response(self, client_id, response_data):
        # print(f"Response from client {client_id}: {response_data}")
        self.all_responses[client_id] = response_data

    def on_finish(self):
        with open("client_responses.json", "w") as json_file:
            json.dump(self.all_responses, json_file, indent=2)


def make_app():
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    print(f"listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
