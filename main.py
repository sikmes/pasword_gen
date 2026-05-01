from fastapi import FastAPI
import random
import string

app = FastAPI()


@app.get("/haslo")
def generuj_haslo(dlugosc: int = 12):
    znaki = string.ascii_letters + string.digits + "!@#$%"
    haslo = "".join(random.choice(znaki) for _ in range(dlugosc))
    return {"haslo": haslo, "dlugosc": dlugosc}
