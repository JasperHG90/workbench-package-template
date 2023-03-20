import os
import pathlib as plb
import tempfile

import pytest
import yaml  # type: ignore
from typer.testing import CliRunner

from {{cookiecutter.__package_slug}}.commands import config

runner = CliRunner()


class TestCheckConfigArg:
    def test_check_config_arg_no_env_var(self):
        value = config._check_config_arg("env", "dev")
        assert value == "dev"

    def test_check_config_arg_raises(self):
        with pytest.raises(
            ValueError,
            match="Input argument 'docker_image_name' must either be passed",
        ):
            if os.getenv("{{ cookiecutter.__package_env_slug }}_DOCKER_IMAGE_NAME") is not None:
                del os.environ["{{ cookiecutter.__package_env_slug }}_DOCKER_IMAGE_NAME"]
            _ = config._check_config_arg("docker_image_name", None)


def test_create_config():
    with tempfile.TemporaryDirectory() as tmpdir:
        result = runner.invoke(
            config.config,
            [
                "create",
                f"{tmpdir}/config.yaml",
                "--env",
                "dev",
            ],
        )
    assert result.exit_code == 0


def test_validate_config(config_dict):
    with tempfile.TemporaryDirectory() as tmpdir:
        path_to_config = plb.Path(tmpdir) / "config.yaml"
        with path_to_config.open("w") as outFile:
            yaml.safe_dump(config_dict, outFile)
            runner.invoke(config.config, ["validate", path_to_config])
