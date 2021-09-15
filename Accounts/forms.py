from django import forms
from .models import Profile

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= '__all__'
        exclude= ('user',)

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields= '__all__'
        exclude= ('user',)
