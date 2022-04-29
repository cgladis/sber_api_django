# serializers.py
from rest_framework import serializers

from .models import Client, ClientData


class ClientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Client
        fields = ('name', 'user')


# class ClientDataSerializer(serializers.Serializer):
class ClientDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientData
        fields = ('client', 'type', 'dt', 'sum')


class ResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    data = serializers.ListField()

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField(max_length=500)
