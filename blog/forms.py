from django import forms
from django.contrib.auth.forms import UserCreationFrom
from django.contrib.auth.models import User
from .models import Blog,Category,Profile,Comment,Tag

class CustomUserCreationFrom(UserCreationFrom):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True,max_length=50)

    class Meta:
        model=User
        fields = ('username', 'first_name','last_name','email','password1','password2')

def save(self,commit=True):
    user = super().save(commit=False)
    user.email = self.cleaned_date['email']
    user.first_name= self.cleaned_date['first_name']
    user.last_name= self.cleaned_date['last_name']

    if commit:
        user.save()

    return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model =Profile
        fields = ['bio','locarion','birth_date','avatar','website']


class BlogsForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','slug','content','featured_image', 'category','tags','is_published']
    
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =['content',]

class TagForm(forms.ModelForm):
    class Meta :
        model =Tag
        fields =['name',]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class Bloglike(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['user','blog']


class UserUpdateForm(forms.ModelForm):
    emial = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']