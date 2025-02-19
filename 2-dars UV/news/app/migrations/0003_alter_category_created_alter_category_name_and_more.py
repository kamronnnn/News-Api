# Generated by Django 5.1.1 on 2024-09-20 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Kategoriya qo'shilgan vaqt"),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Kategoriya nomi'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author_name',
            field=models.CharField(max_length=50, verbose_name='Muallif ismi'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='news',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app.news'),
        ),
        migrations.AlterField(
            model_name='news',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Yangilik qo'shilgan vaqt"),
        ),
    ]
