# fa-proxy

fa-proxy is an HTTP Basic authentication wrapper around Font Awesome's
[private, Pro-only, Python package index](https://docs.fontawesome.com/web/use-with/python-django#using-font-awesome-pro-with-django).
It exists to allow users of [uv](https://docs.astral.sh/uv) and [Poetry](https://python-poetry.org) to use Font Awesome
Pro's Python package in their projects without having to write their Font Awesome Pro package token to `pyproject.toml`.

pip and PDM users have no need for this as those package managers can natively expand environment variables in index
URLs. (Docs: [pip](https://pip.pypa.io/en/stable/reference/requirements-file-format/#using-environment-variables), [PDM](https://pdm-project.org/latest/usage/config/#store-credentials-with-the-index))
uv may be join them in the future (astral-sh/uv#5734). Poetry [will not](https://github.com/python-poetry/poetry/issues/208).

## Usage

### uv

Define an entry for fa-proxy in `[[tool.uv.index]]`:

```toml
# pyproject.toml

[[tool.uv.index]]
name = "fontawesome"
url = "https://fa.celsiusnarhwal.dev/simple"
```

Then, set the `UV_INDEX_FONTAWESOME_PASSWORD` environment variable to your Font Awesome Pro package token (there's no
need to set a username):

```shell
export UV_INDEX_FONTAWESOME_PASSWORD=XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
```

You can now install Font Awesome Pro:

```shell
uv add fontawesomepro
```

### Poetry

Add fa-proxy as an [explicit package source](https://python-poetry.org/docs/repositories#explicit-package-sources)

```shell
poetry source add --priority=explicit fontawesome https://fa.celsiusnarhwal.dev/simple/
```

Then configure its credentials, replacing `<username>` with literally anything and `<token>` with your Font Awesome
Pro package token:

```shell
poetry config http-basic.fontawesome <username> <token>
```
