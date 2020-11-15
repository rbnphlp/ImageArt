 
from django import forms
from .models import Painting, Category
from django.utils.translation import gettext_lazy as _


class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        exclude = ['upload_style_combined','image','rating']
        labels = {
            'upload_pic': _('Upload a Picture'),
            'style_pic': _('Upload a Style  for your Picture'),
            'price':  _('Set a price for your painting (£)')
        }

        widget={

            'Category' : forms.Select(attrs={'class':'form-control'}),
            'price' : forms.NumberInput(attrs={'class':'form-control','minlength':1, 'maxlength': 5, 'required': True, 'type': 'number'}),
            'name' : forms.TextInput(attrs={'class':'form-control','maxlength':100, 'required': True}),
            'description': forms.TextInput(attrs={'class':'form-control','maxlength':100, 'required': True}),

        }
        required = (
            'Category',
            'price',
            'name',
            'description',
        
        )
        

    def __init__(self, *args, **kwargs):

        "overwrite the init method "
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'

