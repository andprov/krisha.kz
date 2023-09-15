import logging

import scr.misc.msg as msg
from db.service import con
from scr.flat import Flat

logger = logging.getLogger()


def insert_flats_data_db(flats_data: list[Flat]) -> None:
    """Insert flats data to DB."""
    insert_flats_query: str = """
        INSERT OR IGNORE
        INTO flats(id,
                   uuid,
                   url,
                   room,
                   square,
                   city,
                   lat,
                   lon,
                   description,
                   photo)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """

    insert_price_query: str = """
        INSERT OR IGNORE
        INTO prices(flat_id, price)
        VALUES (?, ?);
        """

    flats_value: list[tuple] = [
        (
            flat.id,
            flat.uuid,
            flat.url,
            flat.room,
            flat.square,
            flat.city,
            flat.lat,
            flat.lon,
            flat.description,
            flat.photo,
        )
        for flat in flats_data
    ]
    price_value: list[tuple] = [(flat.id, flat.price) for flat in flats_data]

    with con:
        con.executemany(insert_flats_query, flats_value)
        con.executemany(insert_price_query, price_value)
    logger.debug(msg.DB_INSERT_OK)
