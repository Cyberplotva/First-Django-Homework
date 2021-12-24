from django.db import models
from django.db.models.fields import CharField

class Expression(models.Model):
    syntax = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.syntax


class Word(models.Model):
    datetime = models.DateTimeField(auto_now_add=True)
    string = models.CharField(max_length=200)
    word_count = models.IntegerField()
    char_count = models.IntegerField()
    user = CharField(max_length=100)