from django.forms import ModelForm
from .models import ShtuffList

class ShtuffListsForm(ModelForm):
  class Meta:
    model = ShtuffList
    fields = ['name', 'description','image']

