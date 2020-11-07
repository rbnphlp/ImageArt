from django.contrib import admin

from .models import  Category,Style_picture,Uploaded_Picture,Painting

# Register your models here.
admin.site.register(Category)
admin.site.register(Style_picture)
admin.site.register(Uploaded_Picture)
admin.site.register(Painting)



