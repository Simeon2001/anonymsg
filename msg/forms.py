from django import forms
#from django.contrib.auth.models import User
from .models import Comment
#from django.contrib.auth import get_user_model


class CommentForm (forms.ModelForm) :
    
    class Meta :
        model = Comment
        fields=('text',)
        
        
#from .models import Comment
#class CommentForm(forms.ModelForm):
# class Meta:
 #model = Comment
 #fields = ('name', 'email', 'body')
 
 
 