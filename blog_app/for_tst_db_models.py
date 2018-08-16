# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Author(models.Model):
    author = models.CharField(unique=True, max_length=55)

    def __str__(self):
        return self.author

    class Meta:
        managed = False
        db_table = 'author'


class Book(models.Model):
    author = models.ForeignKey(Author, models.DO_NOTHING)
    title = models.CharField(unique=True, max_length=50)
    year_of_writing = models.DateField(blank=True, null=True)

    def __str__(self):
        # return str(self.title + self.author)
        return str(self.title) + '    /    ' + str(self.author)

    class Meta:
        managed = False
        db_table = 'book'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'
