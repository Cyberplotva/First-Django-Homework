from django.db import models

class Expression(models.Model):
    syntax = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.syntax
