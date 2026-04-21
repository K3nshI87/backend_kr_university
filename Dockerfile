FROM python:3.11-slim

# Метаинформация образа (LABEL)
LABEL maintainer="scuvaev67@gmail.com" \
      version="1.0" \
      description="FastAPI Weather Application"

# Создание непривилегированного пользователя (USER)
RUN useradd -m -u 1000 appuser

WORKDIR /app


COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app ./app

EXPOSE 8000

# Проверка здоровья контейнера (HEALTHCHECK)
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/docs')" || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]