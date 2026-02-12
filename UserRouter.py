from fastapi import APIRouter ,Depends
from PydanticModel import UserRequest
from PydanticModel import CreateUserResponse ,UserResponse
from MongoDataBase import get_database
from bson import ObjectId

router = APIRouter(prefix = "/user" ,tags = ["userRouter"])

@router.post("/",response_model = CreateUserResponse)
async def createUsers(user : UserRequest ,db = Depends(get_database)):
    user_dict = user.model_dump(by_alias = True)
    user_dict["fromApi"] = True
    result =await db.users.insert_one(user_dict)
    return {"id" : str(result.inserted_id)}

@router.get("/getone/{userId}",response_model = UserResponse)
async def getUser( userId : str , db = Depends(get_database) ):

    user = await db.users.find_one({ "_id" : ObjectId(userId) })
    user["_id"] = str(user["_id"])
    return user



     


    