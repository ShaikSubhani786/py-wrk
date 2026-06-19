from fastapi import FastAPI
from app.routers import todos

app =  FastAPI(
    title = 'Todo API',
    description = 'A simple API for managing todos',
    version = '0.1.0'
)


app.include_router(todos.router)


@app.get("/")
def root():
    return {
        "message": "Welcome to the Todo API"
    }