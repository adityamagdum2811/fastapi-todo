from fastapi import FastAPI
from app.database.connection import engine, Base
from app.api import auth_routes, todo_routes

def create_app():
    app = FastAPI(title="FastAPI Todo + Auth")
    Base.metadata.create_all(bind=engine)

    app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
    app.include_router(todo_routes.router, prefix="/todos", tags=["todos"])

    @app.get("/")
    def root():
        return {"message": "FastAPI Todo API. Use /docs for UI."}

    return app

# 👇 This line is CRUCIAL
app = create_app()
