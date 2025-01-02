from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class Connection:
    _conn_string = 'mysql+pymysql://%s:%s@%s:%s/%s?charset=utf8mb4'
    _engine = None
    _sessionmaker = None

    def __init__(self, username, password, host, port, db):
        self._engine = create_engine(
            self._conn_string % (username, password, host, port, db),
            pool_size=1,
            max_overflow=0,
            pool_pre_ping=True,
            echo=False
        )
        self._sessionmaker = scoped_session(sessionmaker(bind=self._engine))

    @property
    def session(self):
        return self._sessionmaker()
