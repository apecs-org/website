from django.views.generic import DetailView
from apecs.compass.models import Article


class ArticleDetailView(DetailView):
    template_name = "compass/sites/detail/article.html"
    model = Article
    title = "article"
    context_object_name = "article"