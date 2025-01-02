import tornado.ioloop
from utils.application import Application
from utils.logger import setup_logger

if __name__ == "__main__":
    logger = setup_logger()

    db_config = {
        "username": "artify",
        "password": "artifypwd",
        "host": "db",
        "port": "3306",
        "database": "artify"
    }

    port = 8885
    app = Application(db_config, debug=True)
    app.listen(port)
    logger.info(f"Server running at http://localhost:{port}")
    tornado.ioloop.IOLoop.instance().start()
