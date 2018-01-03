# -*- coding=utf-8 -*-
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=256)
    author = models.CharField(max_length=256)
    type = models.CharField(max_length=256)    # 文章所属类别
    labels = models.CharField(max_length=256)  # 文章标签
    date = models.DateField()
    time = models.TimeField()
    chief = models.CharField(max_length=256)
    image_path = models.CharField(max_length=256)
    content = models.TextField()

    class Meta:
        db_table = 'article'
