from ninja import Schema
from pydantic import UUID4

class MessageOut(Schema):
    detail: str


class UUIDSchema(Schema):
    id: UUID4
    
class postsSchema(Schema):
    title: str
    text: str
    
class posts_out(UUIDSchema,postsSchema):
    pass