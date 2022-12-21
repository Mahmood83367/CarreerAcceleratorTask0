from django.shortcuts import render
from ninja import Router
from taskTable.schemas import MessageOut,tableSchema,table_out
from typing import List
from taskTable.models import Task0Model
from account.authorization import GlobalAuth


task_table = Router()

@task_table.get('Table', auth=GlobalAuth() , response={
    200: List[table_out],
    404: MessageOut
})
def get_table(request,id : str = None):
    if id == None :
        return Task0Model.objects.all()
    else:
        return Task0Model.objects.filter(id=id)
    
    

@task_table.post('list', auth=GlobalAuth() ,response={
    201: table_out,
    422: MessageOut,
    400: MessageOut
})
def create_new_row(request, row_in : tableSchema):
    row = Task0Model(**row_in.dict())
    row.save()
    return 201, row