import logging

import krisha.common.msg as msg
from krisha.db.base import DBConnection

logger = logging.getLogger()


def create_db(connector: DBConnection) -> None:
    """Create DB table."""
    query = """
            CREATE TABLE IF NOT EXISTS flats
            (
                id          INTEGER NOT NULL PRIMARY KEY,
                uuid        TEXT    NOT NULL UNIQUE,
                url         TEXT    NOT NULL,
                room        INTEGER,
                square      INTEGER,
                city        TEXT,
                lat         REAL,
                lon         REAL,
                description TEXT,
                photo       TEXT,
                star        INTEGER DEFAULT 0,
                focus       INTEGER DEFAULT 0
            );
            CREATE TABLE IF NOT EXISTS prices
            (
                id       INTEGER PRIMARY KEY NOT NULL,
                date     DATE DEFAULT (DATE('now', 'localtime')),
                flat_id  INTEGER             NOT NULL,
                price    INTEGER             NOT NULL,
                FOREIGN KEY (flat_id) REFERENCES flats (id),
                UNIQUE (date, flat_id)
            );
            """

    with connector as con:
        con.executescript(query)

    logger.info(msg.DB_CREATED)


def check_sqlite_master(connector: DBConnection) -> bool:
    """Check SQLite master."""
    query = """
            SELECT name
            FROM sqlite_master
            WHERE type = 'table'
              AND name = 'flats';
            """

    with connector as con:
        cursor = con.cursor()
        cursor.execute(query)
        if cursor.fetchone():
            logger.info(msg.DB_OK)
            return True

    return False


def check_db(connector: DBConnection) -> None:
    """Check DB."""
    if not check_sqlite_master(connector):
        create_db(connector)


def get_connection(db_path: str) -> DBConnection:
    """Get DB connection."""
    connection = DBConnection(db_path)
    check_db(connection)
    return connection
