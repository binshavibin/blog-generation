from typing import TypedDict
from pydantic import BaseModel,Field

class Blog(BaseModel):
    title:str = Field(description="title of blog post")
    content:str = Field(description="Main content of blog")

class BlogState(TypedDict):
    topic:str
    blog:Blog
    content_language:str
