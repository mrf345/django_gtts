from django.db import models

class Speech(models.Model):
    text = models.TextField(max_length=2000)
    language = models.TextField(max_length=50)
    file_name = models.TextField(max_length=1000)