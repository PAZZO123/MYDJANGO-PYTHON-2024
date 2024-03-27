from django import forms
from .models import Member

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['firstname', 'lastname', 'phone','joined_date']
