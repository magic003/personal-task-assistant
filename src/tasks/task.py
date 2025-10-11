from pydantic import BaseModel, Field


class Task(BaseModel):
    title: str = Field(..., description="The title of the task.")
