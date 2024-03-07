FROM python3.12
WORKDIR /app
COPY . .
RUN python -m venv .venv
RUN .venv/bin/pip install -r requirements.txt
CMD ["./.venv/bin/uvicorn","app.asgi:app"]
