import typing as t

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pathlib import Path

app = FastAPI()
security = HTTPBasic()


@app.get("/simple/fontawesomepro/{path:path}")
async def proxy(path: Path, credentials: t.Annotated[HTTPBasicCredentials, Depends(security)]):
    return RedirectResponse(f"https://dl.fontawesome.com/{credentials.password}/fontawesome-pro/python/simple/{path}")