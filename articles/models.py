from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

class Comment(models.Model):
    # id =
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # article_id =