from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    is_librarian = models.BooleanField(default=False)
