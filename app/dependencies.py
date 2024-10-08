from typing import Annotated
from fastapi import Header, HTTPException

async def get_token_header(x_token: Annotated[str, Header()]):
    if x_token != "token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")
