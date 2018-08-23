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
    # ---------

    def _get_article_url(self):
        return "/article/%i/" % self.id
    # <h2> <a href = "{{ post.get_absolute_url }}"> {{post.title}} </a> </h2>

    @property
    def article_url(self):
        return self._get_article_url()
    # ---------

    def _get_count_comment(self):
        return Comment.objects.filter(article=self.id).count()

    @property
    def count_comment(self):
        return self._get_count_comment()
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'article'
        # verbose_name = ''
        # verbose_name_plural = ''


class Comment(models.Model):
    article = models.ForeignKey('Article', models.DO_NOTHING)
    content = models.TextField()
    create = models.DateTimeField(auto_now_add=True)  # default=timezone.now
    who_comment = models.ForeignKey(User, models.DO_NOTHING, db_column='who_comment')
    # reply_to_comment_id = models.IntegerField(blank=True, null=True)
    reply_to_comment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return str(self.content)[:30] + ' . . .'

    # ============================ calculated field ============================
    def _get_is_comment(self):
        if self.reply_to_comment is None \
                or self.reply_to_comment == 0\
                or self.reply_to_comment == '':
            return True
        else:
            return False

    @property
    def is_comment(self):
        """check comment (return True) or discussion (return False)"""
        return self._get_is_comment()
    # ---------

    def _get_content_from_parent(self):
        if not self.is_comment:
            parent_id = self.reply_to_comment
            return str(parent_id.content[:30] + '...')

    @property
    def content_from_parent(self):
        """ """
        return self._get_content_from_parent()
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'comment'


class Subscribe(models.Model):
    master_user = models.ForeignKey(User, models.DO_NOTHING, db_column='master_user',
                                    related_name='master_user')
    slave_user = models.ForeignKey(User, models.DO_NOTHING, db_column='slave_user',
                                   related_name='slave_user')

    def __str__(self):
        return str(self.id)

    # ============================ calculated field ============================
    def _get_master_user(self):
        """Returns 'master' user nick """
        return self.master_user.username

    @property
    def master_nick(self):
        return self._get_master_user

    def _get_slave_user(self):
        """Returns 'slave' user nick """
        return self.slave_user.username

    @property
    def slave_nick(self):
        return self._get_slave_user()
    # ==========================================================================

    class Meta:
        managed = False
        db_table = 'subscribe'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
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

    @receiver(post_save, sender=User)
    def create_user(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()
    # ==========================================================================
