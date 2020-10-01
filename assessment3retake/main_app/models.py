from django.db import models
from django.urls import reverse

class Item(models.Model):
    description = models.CharField(max_length=30)

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return reverse('index')