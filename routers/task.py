from fastapi import APIRouter, Depends, Request, status
from database.crud import does_id_exist, fetch_task, fetch_all_task, _create_task, _update_task, remove_task
from response.response import customResponse
from models.model import TaskForm
from exceptions.custom_execption import NotFoundError



router = APIRouter(prefix="", tags=["Task"])


@router.get("/api/task")
async def get_all_tasks(request:Request):
    
    tasks = await fetch_all_task()

    return customResponse(status.HTTP_200_OK, "Fetch all task successfull", data=tasks)




@router.get("/api/task/{task_id}")
async def get_task(request:Request, task_id:str):
    if not await does_id_exist(task_id):
        raise NotFoundError("ID not Found")
    
    task = await fetch_task(task_id)

    return customResponse(status.HTTP_200_OK, "Fetch task successfull", data=task)





@router.post("/api/task")
async def create_task(request:Request, task:TaskForm=Depends()):
    
    
    result = await _create_task(task.title, task.description)

    return customResponse(status.HTTP_201_CREATED, "Created Task", data=result)




@router.put("/api/task/{task_id}")
async def update_task(request:Request, task_id:str, task:TaskForm=Depends()):

    if not await does_id_exist(task_id):
        raise NotFoundError("ID not Found")
    
    await _update_task(task_id, task.title, task.description)

    return customResponse(status.HTTP_200_OK, "Updated Successfully")




@router.delete("/api/task/{task_id}")
async def delete_task(request:Request, task_id:str):

    if not await does_id_exist(task_id):
        raise NotFoundError("ID not Found")


    await remove_task(task_id)

    return customResponse(status.HTTP_200_OK, "Deleted Successfully")





