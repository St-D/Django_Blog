from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Article, Comment


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
        widgets = {'user': forms.HiddenInput()}  # add value in views.py


class RegisterForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    avatar_image = forms.ImageField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'avatar_image']


class CommentForm(forms.Form):

    # def __init__(self, *args, **kwargs):
    #     super(CommentForm, self).__init__(*args, **kwargs)
    #     for visible in self.visible_fields():
    #         visible.field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Comment
        fields = ["content"]
        # fields = '__all__'
        # widgets = {'user': forms.HiddenInput(),
        #            'article_id': forms.HiddenInput(),
        #            'who_comment': forms.HiddenInput(),
        #            'reply_to_comment': forms.HiddenInput(),
        #            }
