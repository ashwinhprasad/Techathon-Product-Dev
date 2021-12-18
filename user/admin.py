from django.contrib import admin
from .models import UserModel, DepartmentModel, SkillModel, AchievementModel, CertificationsModel

# Register your models here.
admin.site.register(UserModel)
admin.site.register(DepartmentModel)
admin.site.register(SkillModel)
admin.site.register(AchievementModel)
admin.site.register(CertificationsModel)