from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.controllers import weather
from prometheus_fastapi_instrumentator import Instrumentator


app = FastAPI()
Instrumentator().instrument(app).expose(app)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(weather.router)