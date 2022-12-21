from ninja import Schema
from pydantic import UUID4

class MessageOut(Schema):
    detail: str


class UUIDSchema(Schema):
    id: UUID4
    
class tableSchema(Schema):
    title: str
    text: str
    
class table_out(UUIDSchema,tableSchema):
    pass