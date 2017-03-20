from rest_framework.routers import DefaultRouter
from retail.views import SequenceViewSet, DetailedSequenceViewSet

router = DefaultRouter()
router.register(prefix='sequences', viewset=SequenceViewSet)
router.register(prefix='detailed-sequences', viewset=DetailedSequenceViewSet)

urlpatterns = router.urls
