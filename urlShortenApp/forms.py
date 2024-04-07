
from .models import *
from django.forms import ModelForm
 

class UrlModelsForm(ModelForm):
  class Meta:
    model =UrlModels
    fields = '__all__'
    exclude =[
      'shortened_url',
      'created_at',
      'updated_at',
      'created_by',
    ]

