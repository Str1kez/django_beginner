from django.db import models
from django.urls import reverse


# Create your models here.
class Article(models.Model):
    """
    model of article in my app with news
    in shell:
        from news.models import Article
        creating:
        Article(...) -> save
        Article.objects.create(...)
        getting:
        Article.objects.all()
        Article.objects.filter(title='...')
        Article.objects.get(pk=...) // requires only one element
        for updating:
        article = Article.objects.get(...)
        article.title = ...
        article.save()
        for deleting:
        article.delete()
        for sorting:
        Article.objects.order_by('title') '-title' for descending
        for excluding data in select:
        Article.objects.exclude(title=...)
    """
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Контент')
    author = models.CharField(max_length=100, verbose_name='Автор')
    image = models.ImageField(upload_to='images/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', verbose_name='Категория', null=True, on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article', kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название категории', db_index=True)

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

