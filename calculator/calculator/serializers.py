from rest_framework import serializers


class NaturalSerializer(serializers.Serializer):
    num = serializers.CharField(max_length=200)
