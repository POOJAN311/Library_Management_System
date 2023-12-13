from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class MyUserManager(BaseUserManager):
    def create_user(self, email, name, phone, address, college, password=None):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone=phone,
            address=address,
            college=college
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone, address, college, password=None):
        user = self.create_user(
            email,
            name,
            phone,
            address,
            college,
            password=password,
        )
        user.is_superuser= True
        user.is_staff  = True
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=25)
    phone = models.CharField(max_length=25)
    address = models.CharField(max_length=25,default='')
    college = models.CharField(max_length=25,default='')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name","phone","address","college"]

    def __str__(self):
        return self.email