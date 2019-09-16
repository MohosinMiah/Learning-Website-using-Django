from django import forms
from django.core import validators



def must_be_empty(value):
    if value:
        raise forms.ValidationError("Must Be Empty")


class SuggesstionForm(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave Empty",validators=[must_be_empty)


    def clean_honeypot(self):
        data = self.cleaned_data["honeypot"]
        if len(data):
            raise forms.ValidationError("Leave It Empty")
        return data
       
