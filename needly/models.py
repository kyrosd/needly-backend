# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    id = models.UUIDField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.TextField(unique=True)
    password = models.TextField()

    class Meta:
        managed = False
        db_table = 'users'


class Inventory(models.Model):
    id = models.UUIDField(primary_key=True)
    user = models.ForeignKey(Users, models.DO_NOTHING)
    inventory_name = models.CharField(max_length=100)
    inventory_description = models.TextField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Items(models.Model):
    id = models.UUIDField(primary_key=True)
    inventory = models.ForeignKey(Inventory, models.DO_NOTHING)
    item_name = models.CharField(max_length=75)
    item_description = models.TextField()
    item_amount = models.IntegerField()
    item_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'
