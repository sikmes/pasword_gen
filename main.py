from fastapi import FastAPI
import random
import string

app = FastAPI()

visit_count = 0

@app.get("/password")
def generate_password(length: int = 12):
    global visit_count
    visit_count += 1
    characters = string.ascii_letters + string.digits + "!@#$%"
    password = "".join(random.choice(characters) for _ in range(length))
    return {"password": password, "length": length, "total_visits": visit_count}

@app.get("/stats")
def get_stats():
    return {"total_visits": visit_count}
