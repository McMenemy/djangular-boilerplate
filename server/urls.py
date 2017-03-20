from rest_framework.routers import DefaultRouter
from retail.views import SequenceViewSet, DetailedSequenceViewSet, ChainViewSet, StoreViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(prefix='sequences', viewset=SequenceViewSet)
router.register(prefix='detailed-sequences', viewset=DetailedSequenceViewSet)
router.register(prefix='chains', viewset=ChainViewSet)
router.register(prefix='stores', viewset=StoreViewSet)
router.register(prefix='employees', viewset=EmployeeViewSet)

urlpatterns = router.urls
