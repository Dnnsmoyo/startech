from django.db import models

# Create your models here.
class Contact(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.subject