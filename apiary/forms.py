from apiary.models import Node, Feature
from django.forms import ModelForm, CharField, TextInput


class NodeForm(ModelForm):
    class Meta:
        model = Node
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(NodeForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class FeatureForm(ModelForm):
    class Meta:
        model = Feature
        fields = '__all__'
