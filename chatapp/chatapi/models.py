from django.db import models
from django.contrib.auth.models import User

# is id the default primary key?
# https://docs.djangoproject.com/en/3.1/topics/db/models/#automatic-primary-key-fields


# Create a User model that has id (auto-incrementing), username, password and is_admin fields
# class User(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     is_admin = models.BooleanField(default=False)


# Create a Group model that has id (auto-incrementing), name and members fields
class Group(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    members = models.ManyToManyField(User)


# Create a Message model that has id (auto-incrementing), group, sender, content and created_at fields
class Message(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
