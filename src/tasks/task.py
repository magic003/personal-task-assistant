from datetime import datetime

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: str | None = Field(
        default=None, description="The unique identifier of the task."
    )
    title: str = Field(description="The title of the task.")
    done: bool = Field(description="Whether the task is completed.", default=False)
    due_time: datetime = Field(description="The due time of the task.")
