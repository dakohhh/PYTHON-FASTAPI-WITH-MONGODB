import motor.motor_asyncio
import bson

client =motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")

#### DATABASE NAME #####
database = client.TaskDB
db = database.task