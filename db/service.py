import logging
import sqlite3

import scr.misc.msg as msg
from scr.config import DB_PATH


logger = logging.getLogger()

con = sqlite3.connect(DB_PATH)
cursor = con.cursor()


def create_db():
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
                flat_id INTEGER             NOT NULL,
                price    INTEGER             NOT NULL,
                FOREIGN KEY (flat_id) REFERENCES flats (id),
                UNIQUE (date, flat_id)
            );
            """

    with con:
        con.executescript(query)


def check_db_exists():
    """Check DB."""
    query = """
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='flats';
            """

    with con:
        cursor.execute(query)
        if cursor.fetchone():
            logger.debug(msg.DB_OK)
            return

    create_db()
    logger.debug(msg.DB_CREATED)
