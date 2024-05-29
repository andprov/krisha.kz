from dataclasses import dataclass

from krisha.config.logs import setup_logs
from krisha.config.parser import ParserConfig, get_parser_config
from krisha.config.path import AppPaths, get_app_path
from krisha.config.search import SearchParameters, get_search_parameters


@dataclass
class Config:
    path: AppPaths
    parser: ParserConfig
    search: SearchParameters


def load_config() -> Config:
    path = get_app_path()
    setup_logs(path)
    parser = get_parser_config()
    search = get_search_parameters(path.search_params_file)
    return Config(path=path, parser=parser, search=search)
