from .database import db
from models.model import TaskModel
from bson import ObjectId
from bson.errors import InvalidId





async def fetch_task(id:str):
    task = await db.find_one({"_id": ObjectId(id)})

    task["_id"] = str(task["_id"])

    return task 


async def fetch_all_task():
    tasks = []

    query = db.find({})
    
    async for task in query:
        
        task['_id'] = str(task['_id'])
    
        tasks.append(task)

    return tasks




async def _create_task(title:str, desc:str):
    task =TaskModel(title=title, description=desc)
    
    result = await db.insert_one(task.dict())
    
    inserted_id = result.inserted_id

    inserted_task = await db.find_one({"_id": inserted_id})

    inserted_task["_id"] = str(inserted_task["_id"])

    return inserted_task




async def _update_task(task_id:str, title:str, desc:str):
    await db.update_one({"_id":ObjectId(task_id)}, {"$set": {"title":title, "description":desc}})




async def remove_task(task_id:str):
    await db.delete_one({"_id":ObjectId(task_id)})




async def does_id_exist(id:str):
    try: 
        object_id = ObjectId(id)

    except InvalidId: 
        
        return False
    

    result = await db.find_one({"_id": ObjectId(id)})


    return False if result is None else True