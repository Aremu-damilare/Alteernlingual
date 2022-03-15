from django import forms
from Alteernlingual_topic.models import  Topic


# class LTLLOIfORM(forms.ModelForm):
#     class Meta:
#         model = LTL_LOI
#         fields = '__all__'


class SubTopicDetailForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'