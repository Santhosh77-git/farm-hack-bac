from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import crops, users, orders

app = FastAPI(title="Farm Hack Backend")

# ✅ Add this CORS block
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # allow all domains (good for testing)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(users.router)
app.include_router(crops.router)
app.include_router(orders.router)

@app.get("/")
def root():
    return {"message": "Farm Hack Backend Running"}