'''
@Author: Sauron Wu
@GitHub: wutianze
@Email: 1369130123qq@gmail.com
@Date: 2020-02-03 14:50:50
@LastEditors  : Sauron Wu
@LastEditTime : 2020-02-05 20:52:12
@Description: 
'''
import tornado.ioloop
import tornado.web

from linuxCmd import*

from tornado.options import define, options
define("port", default=8888, help="run on the given port", type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print(self.request.arguments)
        print(self.get_argument('c',"dd"))
        self.write("Hello")
class ListHandler(tornado.web.RequestHandler):
    def get(self):
        #print(self.request.arguments)
        typeGet = self.get_arguments('type')
        txts = []
        if "status" in typeGet:
            txts.append(server_status())
        if "capability" in typeGet:
            txts.append(server_capability())
        txt = {}
        for key in txts:
            if key["info"] != "success":
                txt = key
                break
            txt.update(key)
        self.write(txt)
def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/list",ListHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
