from django.urls import path

from apecs.compass.app import APECSCompassConfig
from apecs.compass.views.details import ArticleDetailView, GuidebookDetailView, ChapterDetailView
from apecs.compass.views import GuideView

urlpatterns = [
    path("article/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("guidebook/<int:pk>/", GuidebookDetailView.as_view(), name="guidebook-detail"),
    path("chapter/<int:pk>/", ChapterDetailView.as_view(), name="chapter-detail"),
    path('guide/', GuideView.as_view(), name='guide'),
]

app_name = APECSCompassConfig.label
