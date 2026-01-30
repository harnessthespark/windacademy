from rest_framework import serializers
from .models import Client


class ClientListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ("id", "name", "status", "client_type", "industry", "account_manager", "created_at")


class ClientDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
