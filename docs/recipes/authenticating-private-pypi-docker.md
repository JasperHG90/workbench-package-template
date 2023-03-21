# Building and pushing docker images to a private artifact store

When building docker files, the last thing you want to do is leave secrets lying around, which is why it's a good idea to use a multi-stage build process. Unfortunately, it can be a bit annoying to configure authentication to your private pypi repository if you're using one using poetry, since your package is usually installed using `pip`. I've found that the easiest thing to do is to use a .netrc file.

## Generating a .netrc file

Execute the following in a terminal:

```bash
tee -a .netrc << END
machine europe-west4-python.pkg.dev # If using GCP with this region
    login <USERNAME> # If using GCP
    password <PASSWORD>
END
```

## Setting up a multi-stage build using docker

The following build does the following:

1. Creates a new virtual environment
2. Appends the path to the python executable to the PATH
3. Copies the .netrc file and installs the package
4. Copies the .venv to another container and sets updates the PATH variable

```dockerfile
FROM python:3.8-slim as build
# Use same workdir as image to which venv is copied
#  otherwise get problems with CLIs / paths
WORKDIR /opt/workdir
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential gcc
RUN python -m venv /opt/workdir/.venv
ENV PATH="/opt/workdir/.venv/bin:$PATH"
RUN python -m pip install --upgrade pip
# NB: this file is generated in CD
COPY .netrc /root/.netrc
COPY src src
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY README.md README.md
RUN pip install . --extra-index-url=https://europe-west4-python.pkg.dev/this/pypi-registry/simple/

FROM python:3.8-slim
WORKDIR /opt/workdir
COPY --from=build /opt/workdir/.venv .venv
ENV PATH="/opt/workdir/.venv/bin:$PATH"
```

Since the build container is discarded, you are not exposing any secrets.

## In GitHub actions

In GH actions, you can use the following snippet:

```yaml
- name: Generate NETRC file
  env:
    MYPYPI_TOKEN: ${{ secrets.MYPYPI_TOKEN }}
  run: |
    tee -a .netrc << END
    machine europe-west4-python.pkg.dev # If using GCP with this region
        login _json_key_base64 # If using GCP
        password $MYPYPI_TOKEN
    END
```
