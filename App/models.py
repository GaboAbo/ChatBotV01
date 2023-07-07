from django.db import models


class FormModel(models.Model):
    content = models.TextField()

class HistoryModel(models.Model):
    message = models.TextField()
    msgtime = models.TimeField()