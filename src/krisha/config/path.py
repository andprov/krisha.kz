from dataclasses import dataclass


@dataclass
class AppPaths:
    app_dir: str = "krisha"
    logs_dir: str = "logs"
    db_file: str = "db.sqlite"
    logging_config_file: str = "logging.ini"
    search_params_file: str = "SEARCH_PARAMETERS.json"
    parser_config_file: str = "PARSER_CONFIG.json"


def get_app_path() -> AppPaths:
    return AppPaths()
