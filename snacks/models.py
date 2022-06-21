from pydoc import describe
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

class Snack(models.Model):
    title = models.CharField(max_length=255)
    purchaser = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    description = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title