from django import forms
from Alteernlingual_topic.models import LTL_LOI



class LTLLOIfORM(forms.ModelForm):
    class Meta:
        model = LTL_LOI
        fields = '__all__'
