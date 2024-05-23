import logging.config
import os
from logging import Logger

import krisha.common.msg as msg
from krisha.config.path import AppPaths
from krisha.exceptions.config import CreateLogsDirError

logger = logging.getLogger()


def create_logs_dir(file_name: str) -> None:
    try:
        if not os.path.exists(file_name):
            os.makedirs(file_name)
    except OSError as error:
        raise CreateLogsDirError(error) from error


def get_logging_config(file_name: str) -> Logger:
    try:
        logging.config.fileConfig(file_name)
        logger.info(msg.CR_LOGGER_CONFIG_OK)
    except (OSError, KeyError) as error:
        logging.basicConfig(level=logging.DEBUG)
        logger.warning(msg.CR_LOGGER_CONFIG_WRONG.format(error))
    return logging.getLogger()


def setup_logs(path: AppPaths) -> None:
    create_logs_dir(path.logs_dir)
    get_logging_config(path.logging_config_file)
