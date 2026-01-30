from rest_framework import serializers
from .models import Delegate, Trainer, ClientContact


class DelegateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = ("id", "first_name", "last_name", "email", "phone", "employer", "is_candidate", "created_at")


class DelegateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegate
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class TrainerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ("id", "first_name", "last_name", "email", "trainer_type", "day_rate", "created_at")


class TrainerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class ClientContactListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = ("id", "first_name", "last_name", "email", "client", "is_primary", "is_billing", "is_booking")


class ClientContactDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientContact
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
