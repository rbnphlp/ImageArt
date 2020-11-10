 
from django import forms
from .models import Painting, Category
from django.utils.translation import gettext_lazy as _


class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        exclude = ['upload_style_combined','image','price','rating','name','description','category']
        labels = {
            'upload_pic': _('Upload a Picture'),
            'style_pic': _('Upload a Style Picture or Painiting  for your Picture'),
        }
        

    def __init__(self, *args, **kwargs):

        "overwrite the init method "
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


