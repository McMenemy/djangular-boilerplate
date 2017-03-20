from rest_framework import serializers
from retail.models import Sequence

class SequenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sequence
		fields = ('id', 'design', 'description')

class DetailedSequenceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Sequence
		fields = ('id', 'design', 'description', 'formatted_sequence')
