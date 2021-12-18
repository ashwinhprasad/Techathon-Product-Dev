from django.contrib import admin
from .models import QuestionsModel, AnswerModel, HashtagModel

# Register your models here.
admin.site.register(QuestionsModel)
admin.site.register(AnswerModel)
admin.site.register(HashtagModel)
