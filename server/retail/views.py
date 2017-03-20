from rest_framework import viewsets
from retail.models import Sequence, Chain, Store, Employee
from retail.serializers import (
    SequenceSerializer, DetailedSequenceSerializer, ChainSerializer, StoreSerializer, EmployeeSerializer
)

class SequenceViewSet(viewsets.ModelViewSet):
	queryset = Sequence.objects.all()
	serializer_class = SequenceSerializer

class DetailedSequenceViewSet(viewsets.ModelViewSet):
	queryset = Sequence.objects.all()
	serializer_class = DetailedSequenceSerializer

class ChainViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Chain objects """
    queryset = Chain.objects.all()
    serializer_class = ChainSerializer

class StoreViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Store objects """
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Employee objects """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
