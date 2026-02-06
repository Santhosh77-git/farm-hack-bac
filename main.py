from fastapi import FastAPI
from routes import crops, users, orders

app = FastAPI(title="Farm Hack Backend")

app.include_router(users.router)
app.include_router(crops.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Farm Hack Backend Running"}
