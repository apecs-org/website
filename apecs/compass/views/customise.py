from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from apecs.compass.models import Resource
from apecs.compass.models.resource import ResourceCategory, ResourceRegion


class GuideView(TemplateView):
    template_name = "compass/sites/guide/start.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinView(TemplateView):
    template_name = "compass/sites/polarin/polarin.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        context["categories"] = ResourceCategory.objects.all()
        context["resource_stats"] = {
            "resources": Resource.objects.filter(is_active=True).count(),
            "categories": ResourceCategory.objects.count(),
            "regions": ResourceRegion.objects.count(),
        }

        return context


class PolarinTrainingCollectionView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        category = get_object_or_404(
            ResourceCategory,
            slug=self.kwargs["category_slug"],
        )

        context["category"] = category
        context["resources"] = Resource.objects.filter(
            is_active=True,
            categories=category,
        ).order_by("title")

        return context
