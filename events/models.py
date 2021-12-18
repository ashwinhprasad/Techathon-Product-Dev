from django.db import models
from user.models import DepartmentModel

# Create your models here.
class EventsModel(models.Model):
    name = models.CharField(max_length=50)
    organized_by = models.CharField(max_length=100)
    facilitated = models.ForeignKey(DepartmentModel,on_delete=models.CASCADE)
    conducted_on = models.DateField()
    event_desc = models.TextField()

    def __str__(self):
        return f"{self.name} by {self.organized_by}"

class AnnouncementsModel(models.model):
    title = models.CharField(max_length=100)
    info = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title