import httpx
import os
from dotenv import load_dotenv

load_dotenv()  # загружает переменные из .env

API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def get_weather(city: str):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()

    return {
        "city": city,
        "temp": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }