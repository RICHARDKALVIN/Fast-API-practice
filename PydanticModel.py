from pydantic import BaseModel , Field ,ConfigDict
from typing import Optional
from BaseModel import PyObjectId
from bson import ObjectId


class UserRequest(BaseModel):
    name : str
    age : int
    address : str

    model_config = ConfigDict(
        validate_by_name=True,          
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
        

class UserResponse(BaseModel):
    id : Optional[PyObjectId] = Field(alias = "_id")
    name : str
    age : int
    address : str
    fromApi : bool

    model_config = ConfigDict(
        validate_by_name=True,          
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
        
   
class ItemRequest(BaseModel):
    noOfItem : int
    name : str

    model_config = ConfigDict(
        validate_by_name=True,         
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
        
    

class ItemResponse(BaseModel):
    id : Optional[PyObjectId] = Field(alias = "_id")
    noOfItem : int
    name :str
    fromApi : bool

    model_config = ConfigDict(
        validate_by_name=True,         
        arbitrary_types_allowed=True,
        json_encoders={ObjectId: str}
    )
        


class CreateUserResponse(BaseModel):
    id : str

class ItemCreationResponse(BaseModel):
    id : str