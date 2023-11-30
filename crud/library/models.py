from django.db import models

class Book(models.Model):
    Title=models.CharField(max_length=200)
    Author=models.CharField(max_length=200)
    Date_published=models.DateTimeField()
    price=models.IntegerField()

