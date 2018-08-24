from django.http import HttpResponse, HttpResponseRedirect
# from django.template import RequestContext, loader
# from django.template.response import TemplateResponse
# from django.contrib.auth.forms import UserCreationForm
from os import path, listdir
import random

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Article, Subscribe, Comment
from django.contrib.auth.models import User

from .forms import ArticleForm, RegisterForm, CommentForm

# return HttpResponseRedirect(request.META.get('HTTP_REFERER')) //back page
# request.resolver_match.url_name // current url
# @require_http_methods(["POST"])


def random_background():
    """random background from static/img"""
    path_to_project = path.dirname(path.dirname(path.abspath(__file__)))
    path_to_static = path.join(path_to_project, 'static', 'img')
    img_list = listdir(path_to_static)

    return 'img//' + random.choice(img_list)


def index(request):

    page_title = 'Blog Main Page'
    img_background = random_background()
    ten_random_articles = Article.objects.order_by('?')[:10]

    return render(request=request, template_name='index.html', context=locals())


def about(request):
    """render about page"""

    page_title = 'About Page'
    # page_description = 'About Our Blog'
    mail_address = 'mail_to_admin@mail.com'

    return render(request=request, template_name='about.html', context=locals())


def article(request, id):
    """render one article by id"""

    article_by_id = get_object_or_404(Article.objects, pk=id)
    page_title = str(article_by_id.theme).capitalize()
    img_background = random_background()

    all_comments_by_article_obj = Comment.objects.filter(article=id)#.order_by('create')
    comments = all_comments_by_article_obj.filter(reply_to_comment__isnull=True)
    count_comment = all_comments_by_article_obj.count()

    if request.method == "POST":

        form = CommentForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.who_comment = request.user
            response.article = article_by_id

            get_value_from_hidden_field = request.POST.get('id_to_comment')
            if get_value_from_hidden_field:
                response.reply_to_comment = Comment(id=int(get_value_from_hidden_field))

            response.save()

            messages.info(request, '    comment added successfully !')
            return redirect(request.META.get('HTTP_REFERER', '/'))
        else:
            messages.error(request, '    . . . unable to add comment')
            return redirect(request.META.get('HTTP_REFERER', '/'))

    else:
        form = CommentForm()

    return render(request=request, template_name='article.html', context=locals())


def articles_by_user(request, user_pk):
    """sorts and render all articles of the same user"""

    query_user = User.objects.get(pk=user_pk)
    page_title = 'All articles by ' + str(query_user.username).capitalize()
    img_background = random_background()

    article_by_user = Article.objects.all().filter(user=user_pk).order_by('create')

    # return render(request=request, template_name='articles_by_user.html', context=locals())
    return render(request=request, template_name='articles_by_user.html',
                  context={'page_title': page_title,
                           'img_background': img_background,
                           'article_by_user': article_by_user,
                           'int_key_from_url': user_pk})


@transaction.atomic
@login_required
def add_to_favorites(request, user_pk):
    """add user to MyFavorites list. Return info-message on articles_by_user.html"""

    current_loged_user = request.user.id
    return_path = request.META.get('HTTP_REFERER', '/')

    if not Subscribe.objects.filter(master_user=int(user_pk), slave_user=int(current_loged_user)).exists():
        if int(current_loged_user) != int(user_pk):
            create_new_subscriber = Subscribe(
                slave_user=User(id=int(current_loged_user)),
                master_user=User(id=int(user_pk)))

            create_new_subscriber.save()

            messages.info(request, '    add to MyFavorites successfully !')

            return redirect(return_path)
        else:
            messages.info(request, '    . . . why add yourself ?')

            return redirect(return_path)
    else:
        messages.info(request, '    already added . . .')

        return redirect(return_path)


@login_required
def my_favorites(request):
    """"""
    page_title = 'My friends'
    img_background = random_background()

    # for the current user only those -- to whom he is subscribed
    subscribers_val_list = Subscribe.objects.filter(slave_user=request.user.id).values_list('master_user', flat=1)
    favorites_user = User.objects.filter(pk__in=list(subscribers_val_list))

    return render(request=request, template_name='my_favorites.html', context=locals())


@login_required
def all_my_articles(request):
    """render all articles of the current registered user"""

    page_title = 'My articles'
    img_background = random_background()
    article_by_user = Article.objects.all().filter(user=request.user.id)

    return render(request=request, template_name='all_my_articles.html', context=locals())


@login_required
def new_article(request):
    """render form for create new article"""

    page_title = 'Create new article'

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
    return render(request=request, template_name='new_article.html',
                  context={'form': form,
                           'page_title': page_title})


@transaction.atomic
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            user = form.save()
            user.refresh_from_db()
            user.profile.avatar_image = form.cleaned_data.get('avatar_image')
            user.save()

            # login now:
            username = form.cleaned_data.get('username')
            my_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=my_password)
            login(request, user)
            return redirect('index')

    else:
        form = RegisterForm()
    return render(request=request, template_name='register.html',
                  context={'form': form})
