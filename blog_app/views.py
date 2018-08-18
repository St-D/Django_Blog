from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render, get_object_or_404, redirect
from django.template.response import TemplateResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import ArticleForm, RegisterForm
from os import path, listdir
import random

from .models import Article, Profile, Comment, User
# from django.views.generic import ListView, DetailView


# def index(request):
#     form = ArticleForm(request.POST or None)
#     page_title = 'Main Page'
#     user = User.objects.get(id=1)
#     ava = user.avatar_image
#     print(user.avatar_image)
#
#     if request.method == 'POST' and form.is_valid():
#         # debug:
#         # print(request.POST)
#         # print(form.cleaned_data)
#         # print(form.cleaned_data['user'])
#         form.save()
#         # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#
#     return render(request=request, template_name='index.html', context=locals())

def random_background():
    """random background from static/img"""
    path_to_project = path.dirname(path.dirname(path.abspath(__file__)))
    path_to_static = path.join(path_to_project, 'static', 'img')
    img_list = listdir(path_to_static)

    return 'img//' + random.choice(img_list)


def index(request):

    page_title = 'Blog Main Page'
    page_description = 'Blog'
    about_this_page = 'share your ideas with friends and like-minded people'
    img_background = random_background()
    ten_random_articles = Article.objects.order_by('?')[:10]

    return render(request=request, template_name='index.html', context=locals())


def about(request):

    page_title = 'About Page'
    page_description = 'About Our Blog'
    mail_address = 'mail_to_admin@mail.com'

    return render(request=request, template_name='about.html', context=locals())


def article(request, id):
    """render one article by id"""

    article_by_id = get_object_or_404(Article.objects, pk=id)
    page_title = article_by_id.theme
    mail_address = 'mail_to_admin@mail.com'
    img_background = random_background()

    return render(request=request, template_name='article.html', context=locals())


@login_required
def my_favorites(request):

    return render(request=request, template_name='my_favorites.html', context=locals())


@login_required
def all_my_articles(request):

    return render(request=request, template_name='all_my_articles.html', context=locals())


@login_required
def new_article(request):
    """render form for create new article"""

    # if request.user.is_authenticated():
    #     username = request.user.username
    #     print(username)

    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.user = request.user
            response.save()

        return redirect('all_my_articles')
    else:
        form = ArticleForm()
    return render(request=request, template_name='new_article.html', context={'form': form})


# @login_required
@transaction.atomic
def register(request):
    # =============================================================
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print('^1', form.cleaned_data['avatar_img'])
            form.save()
            print('^2',  form.cleaned_data['avatar_img'])

            # login now:
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)

            return redirect('index')
    else:
        form = RegisterForm()
    # =============================================================
    return render(request, 'register.html', {
        'form': form,
        # 'user_form': user_form,
        # 'profile_form': profile_form
    })
    # pass
    # return render(request=request, template_name='register.html', context=locals())

    # u = User.objects.get(username='johny')
    # johny_avatar = u.userprofile.avatar
    # =============================================================


def for_debug(request):
    role = False

    page_title = 'XXXXXXX'
    page_description = 'debug info'
    return render(request=request, template_name='deb.html', context=locals())


def rindex(request):
    article_list = Article.objects.order_by('create')
    # template = loader.get_template('index.html')
    article_list = list(map(lambda x: x.content + '<hr>' + '<br>', article_list))
    # return HttpResponse(article_list)
    # context = RequestContext(request, {
    #     'article_list': article_list,
    # })
    # return HttpResponse(template.render(context))

    # return render(request=request, template_name='index.html',
    #               context={'article_list': article_list})
    return TemplateResponse(request, 'index.html', {'article_list': article_list})


def detail(request, id):

    return HttpResponse("You're voting on question %s." % id)


# def about(request):
#     page_title = "about"
#     form = ArticleForm(request.POST or None)
#
#     return render(request, "about.html", locals())

