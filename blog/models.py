from django.db import models

# Create your models here.
class Drinks(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    price=models.FloatField()
    count=models.IntegerField()
    category=models.ForeignKey('Category', on_delete=models.PROTECT)
    alchogol=models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title=models.CharField(max_length=255)
    text=models.TextField()
    price=models.FloatField()
    count=models.IntegerField()
    category=models.ForeignKey('Category', on_delete=models.PROTECT)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


