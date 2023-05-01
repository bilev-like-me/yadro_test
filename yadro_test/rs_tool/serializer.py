from rest_framework import serializers


class ValidateRequestDataSerializer(serializers.Serializer):
    space_name = serializers.CharField()
    page_name = serializers.CharField()


class ContentSerializer(serializers.Serializer):
    content_data = serializers.CharField()
