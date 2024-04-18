# app/schemas/messages.py
from pydantic import BaseModel

class Msg(BaseModel):
    msg: str
