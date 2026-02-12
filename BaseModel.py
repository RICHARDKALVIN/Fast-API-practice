from bson import ObjectId
from typing import Optional


class PyObjectId(str):
    @classmethod
    def __get_pydantic_core_schema__(cls, _source, _handler):
        from pydantic_core import core_schema
        return core_schema.str_schema()

    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        return handler(core_schema)


