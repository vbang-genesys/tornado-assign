"""

Server details:
-> Tornado Server
-> Database / file system
-> Data preprocessing (clean, fill null)
-> Replace print with logging
-> Add comments and docstrings wherever necessary
-> Apply Black formating to all files

Functions:-
post()
get()
clean()
save_response()
on_finish()

"""


import tornado.ioloop
import tornado.web
import json
import uuid
import logging

logging.basicConfig(
    filename="server_log.log",
    format="%(levelname)s [%(asctime)s] %(name)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S", 
    encoding="utf-8", 
    level=logging.DEBUG)


class MainHandler(tornado.web.RequestHandler):
    all_responses = {}

    async def post(self):
        """
        post(self):-
        -> Load the json file sent by the client
        -> If name or age is null, sent a bad request error (400), else save the json in database/file system
        -> Else generate and send the client ID with status 200
        """
        client_id = str(uuid.uuid4())
        try:
            data = json.loads(self.request.body.decode())
            name = data.get("name", None)
            age = data.get("age", None)
            industry = data.get("industry", "Private")
            salary = data.get("salary", "50000")
            city = data.get("city", "New York")
            if name is None or age is None:
                logging.error("Bad request: Name/age not mentioned.")
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
                self.finish(client_id)
                logging.info(f"Client_id ({client_id}) sent to the client.")

        except json.JSONDecodeError:
            logging.error("Bad request. Json dump not found.")
            self.set_status(400)
            self.finish({"Error": "Invalid json"})

    async def get(self):
        """
        get(self):-
        -> Get client_id
        -> Fetch data from the database/file system
        -> Send the json to the client
        """
        c_id = str(self.get_argument(c_id))
        print(c_id)
        if c_id in self.all_responses:
            logging.info(f"Data with client_id - {c_id} sent.")
            self.finish({self.all_responses[c_id]})
        else:
            logging.error(f"No client with client_id - {c_id} found.")
            self.finish({"Error": "Client not found"})

    def save_response(self, client_id, response_data):
        """Save the response in all_responses"""
        logging.info(f"Response from client {client_id}: {response_data}")
        self.all_responses[client_id] = response_data


    def on_finish(self):
        """On finish save all_responses"""
        with open("client_responses.json", "w") as json_file:
            json.dump(self.all_responses, json_file, indent=2)


def make_app():
    """Returns tornado web application"""
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    port = 8888
    app.listen(port)
    logging.info(f"Listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
