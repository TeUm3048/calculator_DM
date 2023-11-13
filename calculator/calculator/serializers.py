from rest_framework import serializers


class NaturalSerializer(serializers.Serializer):
    num = serializers.CharField(max_length=200)


class IntegerSerializer(serializers.Serializer):
    num = serializers.CharField(max_length=200)


class RationalSerializer(serializers.Serializer):
    num = serializers.CharField(max_length=200)


class PolynomSerializer(serializers.Serializer):
    num = serializers.ListField()
