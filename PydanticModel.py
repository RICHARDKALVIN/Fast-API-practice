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
        
    )
        

class UserResponse(BaseModel):
    id : str = Field(alias = "_id")
    name : str
    age : int
    address : str
    fromApi : bool

    model_config = ConfigDict(
        validate_by_name=True,          
        arbitrary_types_allowed=True,
        
    )
        
   
class ItemRequest(BaseModel):
    noOfItem : int
    name : str

    model_config = ConfigDict(
        validate_by_name=True,         
        arbitrary_types_allowed=True,
        
    )
        
    

class ItemResponse(BaseModel):
    id : str = Field(alias = "_id")
    noOfItem : int
    name :str
    fromApi : bool

    model_config = ConfigDict(
        validate_by_name=True,         
        arbitrary_types_allowed=True,
      
    )
        


class CreateUserResponse(BaseModel):
    id : str

class ItemCreationResponse(BaseModel):
    id : str