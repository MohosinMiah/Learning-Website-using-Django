from django import forms



class SuggesstionForm(forms.Form):
    
    name = forms.CharField()
    email = forms.EmailField()
    suggestion = forms.CharField(widget=forms.Textarea)
    honeypot = forms.CharField(required=False,widget=forms.HiddenInput,label="Leave Empty")


    def clean_honeypot(self):
        

        data = self.cleaned_data["honeypot"]
        if len(data):
            print("ERROR . Leave It EMpty")
        return data
       
