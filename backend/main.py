from fastapi import FastAPI
from backend.api.search import router as search_router

app = FastAPI(title="Deal Intelligence API")

app.include_router(search_router)

@app.get("/")
def root():
    return {"message": "Deal Intelligence API is running 🚀"}
