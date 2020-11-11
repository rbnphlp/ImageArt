from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name





class Painting(models.Model):
    "add a checkbox to add to gallery "

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    upload_pic = models.ImageField(null=True, blank=True,upload_to="Gallery_images/Upload_pic/") 
    style_pic =  models.ImageField(null=True, blank=True,upload_to="Gallery_images/Style_pic/") 
    name = models.CharField(max_length=254,blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    Add_to_Gallery = models.BooleanField(default=True)
    upload_style_combined=models.ImageField(null=True, blank=True,upload_to="Gallery_images/Upload_style_combined/")
    image = models.ImageField(null=True, blank=True,upload_to="Gallery_images/Paintings/")
    

    def __str__(self):
        return self.name
