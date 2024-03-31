from fastapi import APIRouter

from app.schemas.event import Event

router = APIRouter()

@router.post("/event",
             summary="Add an event",
             description="Create a new event",
             responses={
                 200: {"description": "Successful operation"},
                 405: {"description": "Invalid input"}
             })
async def add_event(event: Event):
    # place for some business logic
    return {"message": "Event added successfully"}
