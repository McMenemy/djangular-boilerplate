from rest_framework import viewsets
from retail.models import Sequence
from django.views.generic.base import TemplateView
from retail.serializers import SequenceSerializer, DetailedSequenceSerializer

class SequenceViewSet(viewsets.ModelViewSet):
	queryset = Sequence.objects.all()
	serializer_class = SequenceSerializer

class DetailedSequenceViewSet(viewsets.ModelViewSet):
	queryset = Sequence.objects.all()
	serializer_class = DetailedSequenceSerializer
