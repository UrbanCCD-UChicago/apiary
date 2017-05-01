from apiary.models import Feature
from django.forms import ModelForm


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
