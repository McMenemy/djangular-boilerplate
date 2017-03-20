from rest_framework.routers import DefaultRouter
from retail.views import SequenceViewSet, DetailedSequenceViewSet
from django.conf.urls import url

router = DefaultRouter()
router.register(prefix='sequences', viewset=SequenceViewSet)
router.register(prefix='detailed-sequences', viewset=DetailedSequenceViewSet)

urlpatterns = router.urls
