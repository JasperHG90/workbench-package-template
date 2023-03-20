import logging
import pathlib as plb
import typing

from pydantic import BaseSettings, validator
from pydantic_yaml import YamlModel

logger = logging.getLogger("{{ cookiecutter.__package_slug }}.config")


class GlobalConfig(YamlModel):

    env: str = "dev"

    @validator("env")
    def _check_env(cls, value: str) -> str:
        if value not in ["dev", "stg", "prod"]:
            raise ValueError("'env' must be one of 'dev', 'stg' or 'prod'")
        return value


def load_config(path: typing.Union[str, plb.Path]):
    """Load a YAML configuration file from disk"""
    path = plb.Path(path).resolve()
    if not path.exists():
        raise FileNotFoundError(f"Config at '{path}' not found")
    return GlobalConfig.parse_file(path)
