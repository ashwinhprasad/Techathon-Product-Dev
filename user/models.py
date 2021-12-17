from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self,email,username,phone,password,**other_fields):
        if not email:
            raise ValueError("Email Id Required")
        if not username:
            raise ValueError("Username Required")
        if not phone:
            raise ValueError("Phone Number Required")
        user = self.model(email=self.normalize_email(email),username=username,phone=phone,**other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,email,username,phone,password,**other_fields):
        other_fields.setdefault("is_active",True)
        other_fields.setdefault("is_staff",True)
        other_fields.setdefault("is_superuser",True)
        user = self.create_user(email,username,phone,password,**other_fields)
        user.save()
        return user



class UserModel(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True,max_length=100)
    phone = models.CharField(max_length=10,unique=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    def __str__(self):
        return self.email