# Generated by Django 5.1.1 on 2024-09-20 13:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Kategoriya nomi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name="kategoriya qo'shilgan vaqt")),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Yangilik nomi')),
                ('description', models.TextField(verbose_name='Tavsifi')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name="Yangilisk qo'shilgan vaqt")),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_name', models.CharField(max_length=50, verbose_name='Commentator ismi')),
                ('content', models.TextField(verbose_name='Izoh matni')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Izoh qoldirilgan vaqt')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.news', verbose_name='Yangilik')),
            ],
        ),
    ]
