 
from django import forms
from .models import Painting, Category


class PaintingForm(forms.ModelForm):

    class Meta:
        model = Painting
        fields = '__all__'

        

    def __init__(self, *args, **kwargs):

        "overwrite the init method "
        super().__init__(*args, **kwargs)
        
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


