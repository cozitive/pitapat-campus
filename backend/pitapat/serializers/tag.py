from rest_framework import serializers

from pitapat.models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'type']


class TagIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id']
