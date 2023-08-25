from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # comment_set =

class Comment(models.Model):
    # id =
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE) # 연결된 article이 삭제될 때 관련된 comment가 다 삭제되는 것
    # article_id =