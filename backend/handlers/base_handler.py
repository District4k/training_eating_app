import json

import tornado.web


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db_connection.session

    def get_current_user(self):
        session_data = self.get_secure_cookie("user_session")
        if session_data:
            return json.loads(session_data)
        return None
