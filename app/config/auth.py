import os

SECRET = os.getenv("TOKEN_SECRET", "NahiBataunga")
ALGORITHM = os.getenv("TOKEN_ALG", "HS256")
EXP = int(os.getenv("TOKEN_EXP", 168))
