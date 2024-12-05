from django.db import models

# Create your models here.
class Word(models.Model):
    original_word = models.CharField(max_length=100, unique=True)
    translation = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.original_word} - {self.translation}'