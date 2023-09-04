# Generated by Django 4.2.2 on 2023-07-03 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AddField(
            model_name='articles',
            name='img',
            field=models.ImageField(default='null', upload_to='media/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(verbose_name='Статья'),
        ),
    ]