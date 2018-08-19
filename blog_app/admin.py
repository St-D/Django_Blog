from django.contrib import admin

from .models import Profile, Article, Comment, Subscribe


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["theme", "short_content", "create", "user"]
    search_fields = ['content', 'theme']
    # list_display = [field.name for field in Article._meta.fields]
    # exclude = ['']
    # fields = ['']

    class Meta:
        model = Article

# admin.site.register(Article, ArticleAdmin)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display.append('admin_image')

    list_filter = ['user']
    search_fields = ['user']

    class Meta:
        model = Profile


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'master_nick', 'slave_nick']

    class Meta:
        model = Subscribe


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    search_fields = ['content']

    class Meta:
        model = Comment

