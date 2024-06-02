import logging

import krisha.common.msg as msg
from krisha.crawler.flat_parser import Flat
from krisha.db.base import DBConnection

logger = logging.getLogger()


def insert_flats_data_db(
    connector: DBConnection,
    flats_data: list[Flat],
) -> None:
    """Insert flats data to DB."""
    insert_flats_query = """
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

    insert_price_query = """
        INSERT OR IGNORE
        INTO prices(flat_id, price)
        VALUES (?, ?);
        """

    flats_value = [
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
    price_value = [(flat.id, flat.price) for flat in flats_data]

    with connector as con:
        con.executemany(insert_flats_query, flats_value)
        con.executemany(insert_price_query, price_value)
        con.commit()
    logger.info(msg.DB_INSERT_OK)
