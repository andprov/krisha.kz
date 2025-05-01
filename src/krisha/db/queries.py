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
            flat[0].id,
            flat[0].uuid,
            flat[0].url,
            flat[0].room,
            flat[0].square,
            flat[0].city,
            flat[0].lat,
            flat[0].lon,
            flat[0].description,
            flat[0].photo,
        )
        for flat in flats_data
    ]
    price_value = [(flat[0].id, flat[0].price) for flat in flats_data]

    with connector as con:
        con.executemany(insert_flats_query, flats_value)
        con.executemany(insert_price_query, price_value)
        con.commit()
    logger.info(msg.DB_INSERT_OK)
