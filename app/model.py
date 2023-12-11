from pydantic import BaseModel

class Git(BaseModel):
    token: str
    owner: str
    repo: str