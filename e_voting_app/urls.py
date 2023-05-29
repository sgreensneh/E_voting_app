from django.urls import path, include

from e_voting_app import views
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register('voters', views.VoterViewSet)
router.register('polls', views.PollViewSet)
router.register('parties', views.PartyViewSet)

urlpatterns = router.urls


