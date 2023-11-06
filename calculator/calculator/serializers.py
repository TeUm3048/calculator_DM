from rest_framework import serializers


class NaturalSerializer(serializers.Serializer):
    type = serializers.CharField(max_length=200)
    num = serializers.CharField(max_length=200)
