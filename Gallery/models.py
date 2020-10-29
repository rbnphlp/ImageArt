from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name




class Painting(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name



class Uploaded_Picture(models.Model):
      category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
      upload_pic = models.ForeignKey('Painting', null=True, blank=True, on_delete=models.SET_NULL)  
      name = models.CharField(max_length=254)
      description = models.TextField()
      image_url = models.URLField(max_length=1024, null=True, blank=True)
      image = models.ImageField(null=True, blank=True) 

      def __str__(self):
        return self.name 


class Style_picture(models.Model):
      name = models.CharField(max_length=254)
      description = models.TextField()
      image_url = models.URLField(max_length=1024, null=True, blank=True)
      image = models.ImageField(null=True, blank=True)
      style_pic = models.ForeignKey('Painting', null=True, blank=True, on_delete=models.SET_NULL)  

      def __str__(self):
        return self.name
