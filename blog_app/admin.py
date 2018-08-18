from django.contrib import admin

from .models import Profile, Article, Comment, Subscribe


class ArticleAdmin(admin.ModelAdmin):
    list_display = ["theme", "short_content", "create"]
    search_fields = ['content', 'theme']
    # list_display = [field.name for field in Article._meta.fields]
    # exclude = ['']
    # fields = ['']

    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]
    list_display.append('admin_image')

    list_filter = ['user']
    search_fields = ['user']

    class Meta:
        model = Profile

admin.site.register(Profile, ProfileAdmin)


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['id', 'master_nick', 'slave_nick']

    class Meta:
        model = Subscribe

admin.site.register(Subscribe, SubscribeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Comment._meta.fields]
    search_fields = ['content']

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)
