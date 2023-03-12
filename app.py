from fastapi import FastAPI
from exceptions.custom_execption import *
from routers.task import router as task





app = FastAPI()
app.include_router(task)
app.add_exception_handler(UnauthorizedExecption, unauthorized_exception_handler)
app.add_exception_handler(ServerErrorException, server_exception_handler)
app.add_exception_handler(NotFoundError, not_found)



@app.get("/")
def welcome():
    return {"msg": "Welcome to Fastapi with MongoDB"}
