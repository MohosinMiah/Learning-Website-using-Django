from django import forms
from django.core import validators



def must_be_empty(value):
    if value:
        raise forms.ValidationError("Must Be Empty")


class SuggesstionForm(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave Empty",validators=[must_be_empty])


# Clean method clean entire data 
    def clean(self):
# Get All Data
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        verify_email = cleaned_data.get('verify_email')

        if email != verify_email:
            raise forms.ValidationError("Pls Enter Same EMail")





    # def clean_honeypot(self):
    #     data = self.cleaned_data["honeypot"]
    #     if len(data):
    #         raise forms.ValidationError("Leave It Empty")
    #     return data
       
