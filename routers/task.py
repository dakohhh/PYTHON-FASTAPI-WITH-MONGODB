from fastapi import APIRouter, Depends, Request, status
from database.crud import does_id_exist, fetch_task, fetch_all_task, _create_task
from response.response import customResponse
from models.model import TaskForm, TaskModel
from exceptions.custom_execption import NotFoundError



router = APIRouter(prefix="", tags=["Task"])


@router.get("/api/task")
async def get_all_tasks(request:Request):
    
    tasks = await fetch_all_task()

    return customResponse(status.HTTP_200_OK, "Fetch all task successfull", data=tasks)


@router.get("/api/task/{id}")
async def get_task(request:Request, id:str):
    if not await does_id_exist(id):
        raise NotFoundError("ID not Found")
    
    task = await fetch_task(id)

    return customResponse(status.HTTP_200_OK, "Fetch task successfull", data=task)


@router.post("/api/task")
async def create_task(request:Request, task:TaskForm=Depends()):
    
    
    result = await _create_task(task.title, task.description)

    return customResponse(status.HTTP_200_OK, "Created Task", data=result)


@router.put("/api/task/{id}")
async def update_task(request:Request):
    pass

@router.delete("/api/task/{id}")
async def delete_task(request:Request):
    pass





