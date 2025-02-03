from pydantic import BaseModel
from my_project.users.schemas import UserRegistrationResponse
from datetime import date


class BlogCreateRequestSchema(BaseModel):
    title: str
    content: str


class BlogResponseSchema(BlogCreateRequestSchema):
    date_posted: date

    owner: UserRegistrationResponse

    class Config:
        orm_mode = True


class Message(BaseModel):
    message: str
