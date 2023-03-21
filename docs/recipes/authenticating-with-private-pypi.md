# Authenticating with private PyPI repositories

To authenticate with private PyPI repositories, you need to configure the repo in your `pyproject.toml` and authenticate with it. This is described in the [poetry documentation](https://python-poetry.org/docs/repositories/).

For the examples below, we will assume that the address of the repo is `https://europe-west4-python.pkg.dev/this/pypi-registry/` and the name used to register the repository with poetry is `mypypi`

## Read-only access to the repository

To be able to install from a private PyPI repository, you need to add the following section to your `pyproject.toml`:

```toml
[[tool.poetry.source]]
name = "mypypi"
url = "https://europe-west4-python.pkg.dev/this/pypi-registry/simple/"
default = false
secondary = true
```

You can also add this to your pyproject by executing:

```shell
poetry source add --secondary foo https://europe-west4-python.pkg.dev/this/pypi-registry/simple/
```

## Configuration to push to a private repo

To push packages to a repository, configure the repository as follows (NB: notice that '/simple' is omitted here):

```shell
poetry config repositories.mypypi https://europe-west4-python.pkg.dev/this/pypi-registry/
```

## Configuring authentication

To configure authentication with a private repository, note down your username and password and execute:

```shell
poetry config http-basic.mypypi <username> <password>
```

### Repositories hosted on GCP

For registries hosted on GCP, you can obtain credentials as follows

```shell
gcloud artifacts print-settings python \
    --project=<GCP_PROJECT_ID> \
    --repository=<GCP_ARTIFACT_REGISTRY> \
    --location=europe-west4 \
    --json-key=/path/to/service_account_key.json
```

In this case, your username is `_json_key_base64`, and the password is the base64 encoded key that is returned by the above command

### Repositories hosted on Azure DevOps

For registries hosted on Azure DevOps, you can generate a personal access token and use that as the password. The username doesn't matter.

Construct the URL as `https://pkgs.dev.azure.com/<DEVOPS_ORG_NAME>/_packaging/<DEVOPS_FEED_NAME>/pypi/simple/` for read-only access. If you want to publish packages, it should look as follows: `https://pkgs.dev.azure.com/<DEVOPS_ORG_NAME>/_packaging/<DEVOPS_FEED_NAME>/pypi/upload/`

## Publishing packages to your repository

In your root folder, execute:

```shell
poetry publish -r mypypi --build
```

## Authenticating in GitHub actions

In GH secrets, register the following secret values:

1. MYPYPI_TOKEN: this is the password used to authenticate with your repository
2. MYPYPI_REPO: this is the pypi URL (NB: this should not end with '/simple')

In GH actions, you can use the following action to configure authentication for read/write access to your repo:

```yaml
- name: Authenticate with a private pypi repo
  uses: JasperHG90/toiminnot/poetry-auth-private-pypi@36a879e2095cbc31ae4ac81d6afdc7eb7c0212b7
  with:
    repository_slug: mypypi
    repository_url: ${{ secrets.MYPYPI_REPO }}
    user: _json_key_base64
    password: ${{ secrets.MYPYPI_TOKEN }}
```
