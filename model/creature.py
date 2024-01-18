from pydantic import BaseModel


class Creature(BaseModel):
    name: str
    description: str
    location: str
