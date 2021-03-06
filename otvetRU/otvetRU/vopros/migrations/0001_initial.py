# Generated by Django 4.0.4 on 2022-05-20 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_name', models.CharField(db_index=True, max_length=255, primary_key=True, serialize=False)),
                ('count', models.IntegerField(default=0)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
        ),
        migrations.CreateModel(
            name='Quetion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/&d', verbose_name='Фото')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
                ('isSolved', models.BooleanField(default=False, verbose_name='Решение')),
                ('isPublished', models.BooleanField(default=True, verbose_name='Публикация')),
                ('tag_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vopros.tag', verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=0)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('tume_update', models.DateTimeField(auto_now=True)),
                ('quetionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vopros.quetion')),
            ],
        ),
    ]
