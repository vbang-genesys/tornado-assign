import tornado.ioloop
import tornado.web

class callback(tornado.web.RequestHandler):
    
    def initialize(self):
        self.periodic_callback = tornado.ioloop.PeriodicCallback(self.periodic_task, 1000)
    
    def get(self):
        self.write("Periodic callback:")
    
    def on_finish(self):
        self.periodic_callback.stop()
    
    def periodic_task(self):
        print("Executing periodically...")

if __name__ == "__main__":

    app = tornado.web.Application([(r"/", callback)])
    
    port = 8888
    app.listen(port)
    print(f"listening on port {port}")

    tornado.ioloop.IOLoop.current().start()