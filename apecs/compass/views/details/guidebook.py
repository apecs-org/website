from django.views.generic import DetailView
from apecs.compass.models import Guidebook, Chapter


class GuidebookDetailView(DetailView):
    template_name = "compass/sites/detail/guidebook.html"
    model = Guidebook
    context_object_name = 'guidebook'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch the chapters related to this guidebook, ordered by position
        context['chapters'] = self.object.chapter_set.select_related('article').all()
        return context


class ChapterDetailView(DetailView):
    template_name = "compass/sites/detail/chapter.html"
    model = Chapter
    context_object_name = 'chapter'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get all chapters in the guidebook, ordered by position
        guidebook_chapters = self.object.guidebook.chapter_set.select_related(
            'article').all()
        guidebook_chapters = list(guidebook_chapters)
        current_index = guidebook_chapters.index(self.object)

        # Determine the previous and next chapters
        context['previous_article'] = (
            guidebook_chapters[current_index - 1].article
            if current_index > 0
            else None
        )
        context['next_article'] = (
            guidebook_chapters[current_index + 1].article
            if current_index < len(guidebook_chapters) - 1
            else None
        )

        return context