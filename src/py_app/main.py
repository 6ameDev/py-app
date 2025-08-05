from fastapi import FastAPI
from py_app.routers import ping

app = FastAPI()

routers = [ping.router]

for router in routers:
    app.include_router(router)
