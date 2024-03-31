from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from app.schemas.event import Event
from app.schemas.filter import is_valid_filter_list

router = APIRouter()


@router.get("/analytics/query",
            summary="Get analytics data for events",
            response_model=List[Event],
            responses={
                200: {
                    "description": "Successful operation",
                    "content": {
                        "application/json": {
                            "example": [
                                {
                                    "attribute1": 198772,
                                    "attribute4": "some string",
                                    "date": "2023-01-01T08:00:00",
                                    "metric1": 100,
                                    "metric2": 150.5
                                },
                                {
                                    "attribute1": 198772,
                                    "attribute4": "some string",
                                    "date": "2023-01-01T09:00:00",
                                    "metric1": 120,
                                    "metric2": 160.2
                                }
                            ]
                        }
                    }
                },
                405: {"description": "Invalid input"}
            })
async def get_analytics_data(
    groupBy: str = Query(
        ...,
        description="Attributes for grouping (comma-separated)",
        example="attribute1,attribute4"
    ),
    filters: Optional[str] = Query(
        None,
        description="Array of filters (attribute-value pairs) as JSON string",
        example='[{"attribute": "attribute1", "value": "198772"}, {"attribute": "attribute4", "value": "some string"}]',
    ),
    metrics: str = Query(
        ...,
        description="Metrics to retrieve (comma-separated, always sums)",
        example="metric1,metric2",
    ),
    granularity: str = Query(
        ...,
        description="Granularity (hourly or daily)",
        enum=["hourly", "daily"],
    ),
    startDate: Optional[str] = Query(
        None,
        description="Start date and time for filtering (format: YYYY-MM-DDTHH:mm:ss)",
        example="2023-01-01T08:00:00",
    ),
    endDate: Optional[str] = Query(
        None,
        description="End date and time for filtering (format: YYYY-MM-DDTHH:mm:ss)",
        example="2023-01-01T09:00:00",
    ),
):
    if filters:
        if not is_valid_filter_list(filters):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid format for filters parameter")

    # place for some business logic
    return [
        Event(
            id=1,
            event_date="2024-01-01T08:00:00",
            metric1=198772,
            metric2=1.2,
            attribute1=198772,
            attribute2=198772,
            attribute3=198772,
            attribute4="some string",
            attribute5="12345",
            attribute6=True,
        ),
        Event(
            id=2,
            event_date="2024-02-01T08:00:00",
            metric1=198772,
            metric2=1.2,
            attribute1=198772,
            attribute2=198772,
            attribute3=198772,
            attribute4="some string",
            attribute5="123456",
            attribute6=True,
        ),
    ]
