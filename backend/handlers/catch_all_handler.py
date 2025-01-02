from handlers.base_handler import BaseHandler

class CatchAllHandler(BaseHandler):

    def get(self, *args, **kwargs):
        self.write("Hello world!")
