from fastapi import FastAPI

from app.config.database import Base, engine
from app.config.exception_handlers import register_exception_handlers
from app.config.settings import get_settings
from app.controllers.user_controller import router as user_router

settings = get_settings()

app = FastAPI(title=settings.app_name)

register_exception_handlers(app)
app.include_router(user_router, prefix="/api")


@app.on_event("startup")
def on_startup() -> None:
    Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "UP"}
