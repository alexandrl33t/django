from audioop import reverse as audio_reverse
from cgitb import text
from django.urls import reverse 
from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models
from django.db.models import Count
from django.db import connections
from transliterate import translit
import re

class Quetion(models.Model):
    tittle = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL", blank=True)
    content = models.TextField(blank=False, verbose_name="Контент")
    photo = models.ImageField(upload_to = "photos/%Y/%m/&d", verbose_name="Фото", blank=True)
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")
    isSolved = models.BooleanField(default=False, verbose_name="Решено")
    tag_name = models.ForeignKey('Tag', on_delete=models.PROTECT, verbose_name="Тег")
    author = models.ForeignKey('auth_user', on_delete=models.PROTECT, verbose_name="Автор")
    
    def __str__(self):
        return self.tittle

    def get_absolute_url(self):
        return reverse('quetion', kwargs={'q_slug':self.slug})    
    def save(self, *args, **kwargs):
        self.slug = translit(self.tittle, 'ru', reversed=True)
        text = ''
        for i in range(len(self.slug)):
            if re.match("^[a-zA-Z0-9]*$", self.slug[i]):
                text += self.slug[i]  
        self.slug = text    
        super(Quetion, self).save(*args, **kwargs)
    class Meta():
        verbose_name= 'Вопросы'
        verbose_name_plural = 'Вопросы'
        ordering = ['-time_create', 'tittle']

class Tag(models.Model):
    tag_name = models.CharField(max_length=255, db_index=True, primary_key=True, verbose_name="Категория")
    count = models.IntegerField(default=0, verbose_name="Количество статей")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.tag_name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta():
        verbose_name= 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['tag_name']    

class Answer(models.Model):
    quetionId = models.ForeignKey('Quetion', on_delete=models.CASCADE, verbose_name="id вопроса")  
    content = models.TextField(blank=True, verbose_name="ответ")
    rating = models.IntegerField(default=0, verbose_name="Рейтинг")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    tume_update = models.DateTimeField(auto_now=True, verbose_name="Последнее изменение")