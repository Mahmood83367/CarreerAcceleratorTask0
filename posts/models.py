from django.db import models
import uuid


class Entity(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class PostsModel(Entity):
    title = models.CharField(max_length=255)
    text = models.TextField()
