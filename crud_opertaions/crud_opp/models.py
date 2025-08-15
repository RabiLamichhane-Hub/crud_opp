from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    complete_status = models.BooleanField(default= False)
    due_date = models.DateTimeField()

    def __str__(self):
        return self.name
