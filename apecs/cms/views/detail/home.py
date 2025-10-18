from django.shortcuts import render
from django.views.generic import DetailView
from apecs.cms.models import Home


class HomeDetailView(DetailView):
    template_name = "cms/sites/detail/home.html"
    model = Home
    title = "home"
    context_object_name = "home"

    def get_object(self, queryset=None):
        # Always return the first live Home page
        return Home.objects.live().first()

    def get(self, request, *args, **kwargs):
        home_page = Home.objects.live().first()
        context = home_page.get_context(request)
        return render(request, self.template_name, context)