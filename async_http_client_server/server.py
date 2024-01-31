"""

Server details:
-> Tornado Server
-> Store to mysql database
-> Data preprocessing (clean, fill null, format)
-> Replace print with logging
-> Add comments and docstrings wherever necessary
-> Apply Black formating to all files

Functions:-
post()
get()
clean()
save_response()
log()

"""


import tornado.ioloop
import tornado.web
import json
import uuid
import log_util
import clean_data
import client_database
import os


logger = log_util.get_logger("./logs/server_log.log", __name__)


class MainHandler(tornado.web.RequestHandler):
    async def post(self):
        """
        post(self):-
        -> Load the json file sent by the client
        -> If name or age is null, sent a bad request error (400)
        -> Else generate a new client_id, save the json in the mysql database, and send the client ID with status 200
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
                logger.error("Bad request: Name/age not mentioned.")
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
                response_data = clean_data.clean(response_data)
                if response_data == "bad request":
                    logger.error("Bad request. Unknown city.")
                    self.set_status(400)
                    self.finish({"error": "Input a valid city."})

                else:
                    self.save_response(client_id, response_data)
                    self.finish(client_id)
                    logger.info(f"Client_id ({client_id}) sent to the client.")

        except json.JSONDecodeError:
            logger.error("Bad request. Json dump not found.")
            self.set_status(400)
            self.finish({"Error": "Invalid json"})

    async def get(self):
        """
        get(self):-
        -> Get client_id
        -> Fetch data from the database/file system
        -> Send the json to the client
        """
        c_id = str(self.get_argument("c_id"))
        db = client_database.db_connect()
        cur = db.cursor()
        lookup = client_database.data_lookup(cur, c_id)
        if lookup:
            logger.info(f"Data with client_id - {c_id} sent.")
            self.finish(str(lookup))
        else:
            logger.error(f"No client with client_id - {c_id} found.")
            self.finish({"Error": "Client not found"})
        db.close()

    def save_response(self, client_id, response_data):
        """Save response in the database"""
        db = client_database.db_connect()
        cur = db.cursor()
        logger.info(f"Response from client {client_id}: {response_data}")
        client_database.insert_data(cur, client_id, response_data)
        db.commit()
        db.close()


def make_app():
    """Returns tornado web application"""
    return tornado.web.Application([(r"/", MainHandler)])


if __name__ == "__main__":
    app = make_app()
    port = os.environ.get("port")
    app.listen(port)
    logger.info(f"Listening on port {port}")
    tornado.ioloop.IOLoop.current().start()
