# This is an auto-generated Django model module.

from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Article(models.Model):
    # profile = models.ForeignKey('Profile', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    theme = models.CharField(max_length=255)

    def __str__(self):
        return str(self.content)[:30] + ' . . .'

    # ============================ calculated field ============================
    def _get_short_content(self):
        """Returns the slice content field. Property name `short_content` """
        return str(self.content)[:20] + '...'

    @property
    def short_content(self):
        return self._get_short_content()

    def _get_article_url(self):
        return "/article/%i/" % self.id
    # <h2> <a href = "{{ post.get_absolute_url }}"> {{post.title}} </a> </h2>

    @property
    def article_url(self):
        return self._get_article_url()
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'article'
        # verbose_name = ''
        # verbose_name_plural = ''


class Comment(models.Model):
    article = models.ForeignKey('Article', models.DO_NOTHING)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)
    who_comment = models.ForeignKey('Profile', models.DO_NOTHING, db_column='who_comment')
    # reply_to_comment_id = models.IntegerField(blank=True, null=True)
    reply_to_comment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.content)[:30] + ' . . .'

    class Meta:
        managed = False
        db_table = 'comment'


class Subscribe(models.Model):
    master_user = models.ForeignKey('Profile', models.DO_NOTHING, db_column='master_user',
                                    related_name='master_user')
    slave_user = models.ForeignKey('Profile', models.DO_NOTHING, db_column='slave_user',
                                   related_name='slave_user')

    def __str__(self):
        return self.id

    # ============================ calculated field ============================
    def _get_master_user(self):
        """Returns 'master' user nick """
        return self.master_user.nick

    @property
    def master_nick(self):
        return self.slave_user.nick

    def _get_slave_user(self):
        """Returns 'slave' user nick """
        return self.slave_user.nick

    @property
    def slave_nick(self):
        return self._get_slave_user()
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'subscribe'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # nick = models.CharField(unique=True, max_length=30)
    # mail = models.EmailField(unique=True, max_length=45)
    # md5_password = models.CharField(max_length=255)
    # online_status = models.IntegerField(blank=True, null=True)
    # reg_date = models.DateField(auto_now_add=True)
    avatar_image = models.ImageField(null=True, blank=True, upload_to='avatar_img')

    def __str__(self):
        return self.user.username

    # ============================ calculated field ============================
    def admin_image(self):
        return '<img src="%s" style="width: 50px; border-radius: 5px; box-shadow: 0 0 0 1px #79AEC8, 0 0 5px #333;"/>'\
               % self.avatar_image.url
    admin_image.allow_tags = True
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'profile'


# class Userprofile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar_img = models.ImageField(null=True, blank=True, upload_to='avatar_img')
#     # avatar_img = models.CharField(max_length=255, blank=True)
#
#     def __str__(self):
#         return self.user.first_name
#
#     class Meta:
#         managed = False
#         db_table = 'userprofile'

    # ==========================================================================
    # @receiver(post_save, sender=User)
    # def create_user(sender, instance, created, **kwargs):
    #     if created:
    #         Userprofile.objects.create(user=instance)
    #     instance.userprofile.save()
    # ==========================================================================
