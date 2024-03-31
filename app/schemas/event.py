from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    id: int
    event_date: str
    metric1: int
    metric2: float

    attribute1: Optional[int] = None
    attribute2: Optional[int] = None
    attribute3: Optional[int] = None
    attribute4: Optional[str] = None
    attribute5: Optional[str] = None
    attribute6: Optional[bool] = None
