from fastapi import APIRouter,Depends
from PydanticModel import ItemRequest
from PydanticModel import ItemResponse , ItemCreationResponse
from MongoDataBase import get_database
router = APIRouter(prefix = "/items" ,tags = ["itemsRouter"])

@router.post("/createItem",response_model=ItemCreationResponse)
async def createItems(item : ItemRequest , db = Depends(get_database)):
    item_dict = item.dict()
    item_dict["fromApi"] = True
    result = await db.items.insert_one(item_dict)
    return { "id" :  str(result.inserted_id) }

@router.get("/getone/{userId}",response_model= ItemResponse)
async def  getItemById ( userId : str , db = Depends(get_database)):

    item = await db.items.find_one({"_id" : ObjectId(userId)})
    return item

