from fastapi import FastAPI
from core.config import settings
from starlette.middleware.cors import CORSMiddleware
from api.v1.v1_router import api_v1_router


def create_app() -> FastAPI:
    app = FastAPI(
        debug = settings.Debug,
        title = settings.Title
    )

    register_cors(app = app)
    register_router(app = app)

    return app

def register_cors(app: FastAPI) -> None:
    if settings.Debug:
        app.add_middleware(
            CORSMiddleware,
            allow_origins = ['*'],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

def register_router(app: FastAPI) -> None:
    app.include_router(api_v1_router)
