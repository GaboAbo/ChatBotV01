from django.db import models


class FormModel(models.Model):
    content = models.TextField()