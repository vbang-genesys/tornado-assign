import tornado.ioloop # main event loop
import tornado.web # map requests to requesthandlers
import tornado.httpserver

class helloworld(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

class doc(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class cal(tornado.web.RequestHandler):
    def get(self):
        a = int(self.get_argument("a"))
        b = int(self.get_argument("b"))
        self.write(f"The sum of {a} and {b} is {a+b}")

if __name__ == "__main__":
    app = tornado.web.Application([(r"/", helloworld),
                                   (r"/doc", doc),
                                   (r"/cal", cal)], debug=True, autoreload=True)
    port = 8880
    app.listen(port)
    print(f"listening on port {port}")
    tornado.ioloop.IOLoop.current().start() # to start the current thread