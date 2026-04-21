from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from app.services.weather_service import get_weather
from app.core.templates import templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request,
        "index.html",
        {}
    )


@router.get("/weather", response_class=HTMLResponse)
async def weather(request: Request, city: str):
    data = await get_weather(city)

    return templates.TemplateResponse(
        request,
        "index.html",
        {"weather": data}
    )