from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField(max_length=100, verbose_name='博客分类')

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    标签Tag
    """
    name = models.CharField(max_length=100, verbose_name='标签名')

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    文章数据
    """
    title = models.CharField(max_length=40, verbose_name='标题')
    body = models.TextField(verbose_name='正文')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='摘要')
    category = models.ForeignKey(Category, verbose_name='分类', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    author = models.ForeignKey(User, verbose_name='作者', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_time']

