# Workbench python template: a tagline that sounds hip and cool and convinces you

<!--
[![Documentation Status](https://readthedocs.org/projects/py-pkgs-cookiecutter/badge/?version=latest)](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/)
![tests](https://github.com/py-pkgs/py-pkgs-cookiecutter/workflows/test/badge.svg)
[![release](https://img.shields.io/github/release/py-pkgs/py-pkgs-cookiecutter.svg)](https://github.com/py-pkgs/py-pkgs-cookiecutter/releases)
[![python](https://img.shields.io/badge/python-%5E3.8-blue)]()
[![os](https://img.shields.io/badge/OS-Ubuntu%2C%20Mac%2C%20Windows-purple)]()
-->

This is a poetry package template used for creating python packages using modern development tools.

This package template was adapted from [the py-pkgs cookiecutter template](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/) by Thomas Beuzen.

## Features

This template uses the following tools for development, code quality & testing:

- `Poetry` (obviously)
- `Pre-commit` to run static checks on code
- `Black` for code formatting
- `Isort` for sorting dependencies
- `Codespell` for correcting spelling
- `Ruff` for linting
- `Pyproject-fmt` to format pyproject.toml
- `Interrogate` for docstring coverage
- `Deptry` to check for possible package conflicts
- `Mypy` for type hint checking
- `Nox` & `nox-poetry` for testing across python versions
- `Invoke` for defining re-usable / useful commands
- `Python-semantic-release` for versioning based on git commits
- `sync_with_poetry` pre-commit hook to keep parity between dev package versions and pre-commit revs.

Additionally, this package template contains starter code using:

- `typer` for creating CLIs
- `pydantic_yaml` for creating/parsing YAML config files

## Recipes

Depending on how you want to use the template, you can find additional setup in the [recipes](recipes/) subsection of the docs.

## Usage

Please see the [documentation](https://jasperhg90.github.io/workbench-package-template/) for more detail on using `workbench-package-template`. We provide the fundamental steps below:

1. Install [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/):

    ```bash
    pip install cookiecutter
    ```

1. Generate a Python package structure using [`workbench-package-template`](https://github.com/JasperHG90/workbench-package-template):

    ```bash
    cookiecutter https://github.com/JasperHG90/workbench-package-template.git
    ```

### First steps

1. Create a GH repository and do the following:

1. Enable GH pages by going to Settings > Pages and selecting Source as 'GitHub actions', then selecting 'Static HTML'. Cancel the action that is created for you (this is already incorporated in the template).

![](static/gh-pages.png)

1. Run `poetry install`

1. Check in the changes and push to main with the commit message 'ci skip'

1. Run `poetry shell`

1. Run `invoke set-up-pre-commit` to set up the pre-commit hooks

## Contributing

Interested in contributing? Check out the [Contributing Guidelines](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/contributing.html). Please note that this project is released with a [Code of Conduct](https://py-pkgs-cookiecutter.readthedocs.io/en/latest/conduct.html). By contributing to this project, you agree to abide by its terms.

## License

`py-pkgs-cookiecutter` was created by Tomas Beuzen and Tiffany Timbers. It is licensed under the terms of the BSD license.

## Acknowledgements

`py-pkgs-cookiecutter` was originally developed for use in the University of British Columbia's (UBC) `Master of Data Science`_ program (MDS). It was inspired by the pyOpenSci `cookiecutter` [template](https://github.com/pyOpenSci/cookiecutter-pyopensci).
