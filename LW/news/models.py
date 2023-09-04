from django.db import models
from django.utils import timezone

class Articles(models.Model):
    name = models.CharField('Название', max_length=50)
    title = models.CharField('Название статьи', max_length=250)
    text = models.TextField('Статья')
    data = models.DateTimeField('Дата создания', default=timezone.now)
    img = models.ImageField('Изображение', upload_to='images/', default='null')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"



