from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ArticleForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Article
        fields = ["theme", "content"]
        # fields = '__all__'
        # exclude = [""]
        widgets = {'user': forms.HiddenInput()}


class RegisterForm(UserCreationForm):
    # avatar_img = forms.CharField(max_length=255)
    avatar_img = forms.ImageField(required=False)
    # class Meta(UserCreationForm.Meta):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'avatar_img']

    def save(self, commit=False):
        user = super(RegisterForm, self).save()
        user_profile = Userprofile(user=user, avatar_img=self.cleaned_data['avatar_img'])
        user.save()
        user.refresh_from_db()
        user_profile.save()
        # return user, user_profile

