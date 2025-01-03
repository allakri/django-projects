from django.db import models

# Create your models here.
class Products(models.Model):
    def __str__(self):
        return self.title
    
    title = models.CharField(max_length=200)
    price = models.FloatField()
    discount = models.FloatField()
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=500)


class Order(models.Model):
    # Store product IDs as a string of comma-separated values
    items = models.CharField(max_length=900,default='')  # Store product IDs in this field
    name = models.CharField(max_length=100)
    email = models.EmailField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.IntegerField()
    contact = models.CharField(max_length=15)

    def __str__(self):
        return f"Order by {self.name} ({self.id})"
