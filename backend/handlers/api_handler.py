from handlers.base_handler import BaseHandler
from tornado.escape import json_encode

class APIHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write(json_encode(dict(success=1)))
