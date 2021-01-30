from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from aioredis import create_redis_pool


from api.v1.v1_router import api_v1_router
from core.config import settings



def create_app() -> FastAPI:
    app = FastAPI(
        debug = settings.Debug,
        title = settings.Title
    )

    register_cors(app = app)
    register_router(app = app)
    register_redis(app = app)

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

def register_redis(app: FastAPI) -> None:
    """
    把redis挂载到app对象上面
    :param app:
    :return:
    """
    # 启动事件
    @app.on_event('startup')
    async def startup_event():
        """
        获取链接
        :return:
        """
        app.state.redis = await create_redis_pool(settings.REDIS_URL)
    # 关闭事件
    @app.on_event('shutdown')
    async def shutdown_event():
        """
        关闭
        :return:
        """
        app.state.redis.close()
        await app.state.redis.wait_closed()
