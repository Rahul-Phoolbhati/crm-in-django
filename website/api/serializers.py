# Create model Serializerz, response oj cant natively handle complex dta type suchas django instances
from rest_framework import serializers
from website.models import Record

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'