from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'url', 'cat', 'image']

    title = forms.CharField(max_length=200)
    content = forms.CharField(widget=CKEditorWidget())
    url = forms.CharField(max_length=100)
    cat = forms.ModelChoiceField(queryset=Category.objects.all())
    image = forms.ImageField()
    #
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['cat'].empty_label = 'Select Category'


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
