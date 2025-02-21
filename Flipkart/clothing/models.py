from django.db import models

# Create your models here.
class Product(models.Model):
    Size_choices=[
        ('S','Small'),
        ('M','Medium'),
        ('L','Large'),
        ('XL','Extar Large')
    ]
    Colour_choices=[
        ('Red','Red'),
        ('Blue','Blue'),
        ('Green','Green'),
        ('Black','Black'),
        ('White','White'),
    ]
    name=models.CharField(max_length=200)
    size=models.CharField(max_length=2, choices=Size_choices,default='M')
    colour=models.CharField(max_length=10, choices=Colour_choices,default='Red')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    image=models.ImageField(upload_to='product_img/')