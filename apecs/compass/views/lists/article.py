from django.views.generic import ListView

from apecs.compass.models import Article


class ArticleListView(ListView):
    template_name = "compass/sites/list/article_list.html"
    model = Article
    title = "article"
    context_object_name = "article_list"