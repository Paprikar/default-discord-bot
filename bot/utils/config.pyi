from logging import Formatter
from logging import Logger
from typing import Tuple


def parse_config(config_path: str, logger: Logger, formatter: Formatter) -> Tuple[str, str, int, dict]: ...