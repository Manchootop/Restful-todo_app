from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.

UserModel = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=15,
    )


class Task(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()

    state = models.BooleanField(default=False, blank=True, null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
