import tornado

from handlers.api_handler import APIHandler
from handlers.catch_all_handler import CatchAllHandler
from handlers.load_sectors import LoadSectorsHandler
from handlers.form_handler import FormHandler

class Application(tornado.web.Application):
    db_connection = None

    def __init__(self, db_config, **settings):
        handlers = [
            (r"/api/save", FormHandler),
            (r"/api/load_last_session", FormHandler),
            (r"/api/load_sectors", LoadSectorsHandler),
            (r"/api(.*)", APIHandler),
            (r"/(.*)", CatchAllHandler),
        ]
        super().__init__(handlers, **settings)

        from utils.database import Connection
        self.db_connection = Connection(
            username=db_config["username"],
            password=db_config["password"],
            host=db_config["host"],
            port=db_config["port"],
            db=db_config["database"]
        )
