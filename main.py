import uvicorn
from fastapi import FastAPI, Response, Request
from fastapi.middleware.cors import CORSMiddleware

from src.core import config
from src.app import routers
from src.db.session import SessionLocal


app = FastAPI(
    title="Useful",
    description="Author - DJWOMS",
    version="0.0.1",
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=config.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

app.include_router(routers.api_router, prefix=config.API_V1_STR)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8080, debug=True)
