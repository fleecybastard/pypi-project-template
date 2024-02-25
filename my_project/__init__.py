from pydantic import BaseModel


class Project(BaseModel):
    author: str
    desc: str
