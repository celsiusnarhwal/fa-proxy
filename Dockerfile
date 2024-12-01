FROM ghcr.io/astral-sh/uv:0.5-debian

WORKDIR /app/

COPY . /app/

RUN uv sync

CMD ["uv", "run", "fastapi", "run", "api/index.py"]