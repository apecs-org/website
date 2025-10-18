from django.db import models
from apecs.compass.models.article import Article


class Guidebook(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=200, default='')

    articles = models.ManyToManyField(Article, default='na', through="Chapter")

    def __str__(self):
        return self.title


class Chapter(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    guidebook = models.ForeignKey(Guidebook, on_delete=models.CASCADE)
    position = models.IntegerField()

    class Meta:
        unique_together = [['guidebook', 'article']]
        ordering = ['position',]

    def __str__(self):
        return str(self.guidebook) + ' ' + str(self.position) + ' - ' + str(self.article)
