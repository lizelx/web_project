# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Dict(models.Model):
    id = models.AutoField(primary_key=True)
    angl = models.TextField(blank=True, null=True)
    rus = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dict'


class Dict_custom(models.Model):
    id = models.AutoField(primary_key=True)
    angl = models.TextField(blank=True, null=True)
    rus = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'dict_custom'


class Customs(models.Model):
    firstName = models.TextField(blank=True, null=True)
    lastName = models.TextField(blank=True, null=True)
    username = models.TextField(blank=True, null=True)
    email = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'customs'