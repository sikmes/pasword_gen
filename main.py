from fastapi import FastAPI
import random
import string

app = FastAPI()


@app.get("/password")
def generate_password(length: int = 12):
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(random.choice(characters) for _ in range(length))
    return {"password": password, "length": length}
