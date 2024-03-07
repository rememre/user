import os

from dotenv import load_dotenv

load_dotenv()

origins = {
    "dev": [
        "http://localhost:5173",
    ],
    "prod": [
        # Live Consumer URL(s)
    ]
}

class Base:
    env = os.getenv("ENVIRONMENT", "dev")
    name = os.getenv("NAME", "development")
    url = os.getenv("URL", "user_service")
    origins = origins.get(env)
