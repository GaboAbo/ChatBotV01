from django.db import models
from django.contrib.auth.models import User


class FormModel(models.Model):
    content = models.TextField()

class HistoryModel(models.Model):
    message = models.TextField()
    msgtime = models.TimeField()

    user    = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ["msgtime"]