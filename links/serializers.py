from dataclasses import fields
from rest_framework import serializers
from .models import Link



class LinkSerializer(serializers.ModelSerializer):
    short_url=serializers.ReadOnlyField()

    class Meta:
        model=Link
        fields='__all__'