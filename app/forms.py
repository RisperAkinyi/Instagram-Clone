from django import forms
from .models import Comments, Profiles, Images

class PostImageForm(forms.ModelForm):
    image = forms.ImageField()
    caption = forms.CharField(max_length=100)
    class Meta: 
        model = Images
        exclude = ['posted','profile']
    
class PostComment(forms.ModelForm):
    # comment = forms.CharField(label='Leave a comment',max_length=100)
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']

class PostProfile(forms.ModelForm):
    # bio = forms.CharField(label='Leave a comment',max_length=100)
    class Meta:
        models = Profiles
        exclude = ['user',]
    