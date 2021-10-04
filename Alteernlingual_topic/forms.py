from django import forms
from Alteernlingual_topic.models import  SubTopicDetails



# class LTLLOIfORM(forms.ModelForm):
#     class Meta:
#         model = LTL_LOI
#         fields = '__all__'


class SubTopicDetailForm(forms.ModelForm):
    class Meta:
        model = SubTopicDetails
        fields = '__all__'