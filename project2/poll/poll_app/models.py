from django.db import models

# Create your models here.
class MenuCategory(models.Model):
    category_name = models.CharField(max_length=20)

class Menu(models.Model):
    name = models.CharField(max_length=50) 
    category_id = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        default=None
    )
    price = models.IntegerField() 


