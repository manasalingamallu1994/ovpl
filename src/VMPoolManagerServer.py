mport urlparse
import os
import sys
import os.path
import json

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options
#import LabManager 
import VMPoolManager
import Logging


define("port", default=8000, help="run on the given port", type=int)


class CreateVMHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('trying to create a vm')

    def post(self):
        post_data = dict(urlparse.parse_qsl(self.request.body))
        vmpoolmgr=VMPoolManager.VMPoolManager()
        Logging.LOGGER.debug("Controller: test_lab(); invoking create_vm() on vmpoolmgr")
        lab_state=vmpoolmgr.create_vm(json.loads(post_data['lab_spec']))
        Logging.LOGGER.debug("Controller: test_lab(): Returned from VMPool = %s" % (str(lab_state)))
        self.write(lab_state)


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r"/", CreateVMHandler)
        ],
        debug = True)
http_server = tornado.httpserver.HTTPServer(app)
http_server.listen(8080)
tornado.ioloop.IOLoop.instance().start()

                      
