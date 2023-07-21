from pydantic import BaseModel


class FibResponse(BaseModel):
    number: int
    fibonacci: int
