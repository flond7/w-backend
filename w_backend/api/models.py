from djongo import models
import uuid 

class path(models.Model):
  _id = models.ObjectIdField() 
  pathId = models.UUIDField(primary_key=False, unique=True, default=uuid.uuid4, editable=False)
  start = models.DateField()
  end = models.DateField(blank=True, )
  
  class Meta:
    ordering = ['start']

  def __str__(self):
    return self.title

class woman(models.Model):
  name = models.CharField(max_length=100, blank=True, default='')
  surname = models.CharField(max_length=100, blank=True, default='')
  path = models.ArrayField(model_container=path)
  
  class Meta:
    ordering = ['name']

  def __str__(self):
    return self.title