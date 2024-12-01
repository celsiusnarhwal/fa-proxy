import typing as t

from fastapi import Depends, FastAPI
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()
security = HTTPBasic()


@app.get("/")
async def root():
    return RedirectResponse("https://github.com/celsiusnarhwal/fa-proxy")


@app.get("/{path:path}")
async def proxy(
    path: str, credentials: t.Annotated[HTTPBasicCredentials, Depends(security)]
):
    return RedirectResponse(
        f"https://dl.fontawesome.com/{credentials.password}/fontawesome-pro/python/{path}"
    )
