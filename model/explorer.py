from pydantic import BaseModel

class Explorer(BaseModel):
    name: str
    nationality: str