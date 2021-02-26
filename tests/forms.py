from django.forms import ModelForm
from product.models import test

class TestForm(ModelForm):
    class Meta:
        model = test
        fields='__all__'
