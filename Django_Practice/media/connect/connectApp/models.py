from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length = 255)
    image = models.FileField(upload_to='images/')
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.title
# Create your models here.
