from django.views.generic import TemplateView


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
        return context


class PolarinTrainingCollectionView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-template.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context

class PolarinTrainingCollectionPlanningView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-planning.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionSafetyView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-safety.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionLogisticsView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-logistics.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionCollaborationView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-collaboration.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionEnvironmentView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-environment.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionInstrumentsView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-instruments.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionDataView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-data.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context


class PolarinTrainingCollectionCommunicationView(TemplateView):
    template_name = "compass/sites/polarin/polarin-collection-communication.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation to get the default context
        context = super().get_context_data(**kwargs)
        return context