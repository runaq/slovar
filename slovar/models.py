from django.conf import settings
from django.db import models
from django.utils import timezone

class Tags(models.Model):
    tag = models.CharField(max_length=200)
    def __str__(self):
        return str(self.tag)
        
class Words(models.Model):
    tag = models.ForeignKey(Tags, on_delete=models.SET_NULL, blank=True,  null=True  )
    slov = models.CharField(max_length=200, unique=True)
    rus = models.CharField(max_length=200)
   
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slov = self.slov.title()  # Переводим значение в верхний регистр
        self.rus = self.rus.title()
        return super(Words, self).save(force_insert, force_update, using, update_fields)
        
    def __str__(self):
        return str(self.rus)