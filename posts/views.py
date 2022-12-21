from django.shortcuts import render
from ninja import Router
from posts.schemas import MessageOut,postsSchema,posts_out
from typing import List
from posts.models import PostsModel
from account.authorization import GlobalAuth


posts_controller = Router()

@posts_controller.get('posts', auth=GlobalAuth() , response={
    200: List[posts_out],
    404: MessageOut
})
def get_posts(request,id : str = None):
    if id == None :
        return PostsModel.objects.all()
    else:
        return PostsModel.objects.filter(id=id)
    
    

@posts_controller.post('posts', auth=GlobalAuth() ,response={
    201: posts_out,
    422: MessageOut,
    400: MessageOut
})
def create_new_post(request, post_in : postsSchema):
    post = PostsModel(**post_in.dict())
    post.save()
    return 201, post