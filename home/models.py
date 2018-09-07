# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Applications(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    color = models.TextField(blank=True, null=True)
    defaultstatus = models.IntegerField(blank=True, null=True)
    link = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'applications'

class Users(models.Model):
    pid = models.IntegerField(primary_key=True)
    login = models.TextField(blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'


class Userapps(models.Model):
    pid = models.IntegerField(primary_key=True)
    placeorder = models.IntegerField(blank=True, null=True)
    userid = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='userid')
    appid = models.ForeignKey(Applications, on_delete=models.CASCADE, db_column='appid')

    class Meta:
        managed = True
        db_table = 'userapps'

