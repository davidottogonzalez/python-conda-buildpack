import tornado.ioloop
import tornado.web
import os

#just a demo use of the library in the code
from impala.dbapi import connect

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, Conda")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen( int(os.getenv("PORT")) )
    tornado.ioloop.IOLoop.current().start()
