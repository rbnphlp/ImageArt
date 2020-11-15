from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name





class Painting(models.Model):
    "add a checkbox to add to gallery "

    category = models.ForeignKey('Category', null=True, blank=False, on_delete=models.SET_NULL)
    upload_pic = models.ImageField(null=True, blank=False,upload_to="Gallery_images/Upload_pic/") 
    style_pic =  models.ImageField(null=True, blank=False,upload_to="Gallery_images/Style_pic/",default="Style_pic/default_style.jpg") 
    name = models.CharField(max_length=254,blank=False)
    description = models.TextField(blank=False)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=False,null=True,validators=[MinValueValidator(0)])
    rating = models.IntegerField( null=True, blank=True, validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ])
    Add_to_Gallery = models.BooleanField(default=True)
    upload_style_combined=models.URLField(null=True, blank=True)
    image = models.URLField(null=True, blank=True)
    

    def __str__(self):
        return self.name
