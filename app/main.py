import uvicorn
from fastapi import FastAPI

from app.routers import analytics, event

app = FastAPI()

app.include_router(event.router)
app.include_router(analytics.router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
