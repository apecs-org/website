from django.views.generic import TemplateView


class GuideView(TemplateView):
    template_name = "compass/sites/guide/start.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context