from django.urls import path

from apecs.compass.app import APECSCompassConfig
from apecs.compass.views.details import ArticleDetailView, GuidebookDetailView, \
    ChapterDetailView
from apecs.compass.views import GuideView, PolarinView, \
    PolarinTrainingCollectionView, \
    PolarinTrainingCollectionCommunicationView, \
    PolarinTrainingCollectionPlanningView, \
    PolarinTrainingCollectionDataView, \
    PolarinTrainingCollectionSafetyView, \
    PolarinTrainingCollectionLogisticsView, \
    PolarinTrainingCollectionCollaborationView, \
    PolarinTrainingCollectionEnvironmentView, \
    PolarinTrainingCollectionInstrumentsView

urlpatterns = [
    path("article/<int:pk>/", ArticleDetailView.as_view(),
         name="article-detail"),
    path("guidebook/<int:pk>/", GuidebookDetailView.as_view(),
         name="guidebook-detail"),
    path("chapter/<int:pk>/", ChapterDetailView.as_view(),
         name="chapter-detail"),
    path('guide/', GuideView.as_view(), name='guide'),
    path('polarin-training/', PolarinView.as_view(), name='polarin-training'),
    path('polarin-training/collection-template',
         PolarinTrainingCollectionView.as_view(),
         name='polarin-training-collection-template'),
    path('polarin-training/planning',
         PolarinTrainingCollectionPlanningView.as_view(),
         name='polarin-training-collection-planning'),
    path('polarin-training/safety',
         PolarinTrainingCollectionSafetyView.as_view(),
         name='polarin-training-collection-safety'),
    path('polarin-training/logistics',
         PolarinTrainingCollectionLogisticsView.as_view(),
         name='polarin-training-collection-logistics'),
    path('polarin-training/collaboration',
         PolarinTrainingCollectionCollaborationView.as_view(),
         name='polarin-training-collection-collaboration'),
    path('polarin-training/environment',
         PolarinTrainingCollectionEnvironmentView.as_view(),
         name='polarin-training-collection-environment'),
    path('polarin-training/instruments',
         PolarinTrainingCollectionInstrumentsView.as_view(),
         name='polarin-training-collection-instruments'),
    path('polarin-training/data',
         PolarinTrainingCollectionDataView.as_view(),
         name='polarin-training-collection-data'),
    path('polarin-training/communication',
         PolarinTrainingCollectionCommunicationView.as_view(),
         name='polarin-training-collection-communication'),
]

app_name = APECSCompassConfig.label
