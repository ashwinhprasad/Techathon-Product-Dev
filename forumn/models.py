from django.db import models
from user.models import UserModel

# Create your models here.
class QuestionsModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    asked_by = models.ForeignKey(UserModel,on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.title} - {self.id}"

class AnswerModel(models.Model):
    question = models.ForeignKey(QuestionsModel, on_delete=models.CASCADE)
    answer = models.TextField()
    answer_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.answer} - {self.id}"

class HashtagModel(models.Model):
    tagname = models.CharField(max_length=20, primary_key=True)
    question = models.ManyToManyField(QuestionsModel, blank=True)
    def __str__(self):
        return self.tagname