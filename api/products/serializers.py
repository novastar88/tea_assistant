from rest_framework import serializers
from .models import *


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
        read_only_fields = ["id"]


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = "__all__"
        read_only_fields = ["id"]


class ContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Container
        fields = "__all__"
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    status = StatusSerializer
    shop = CompanySerializer

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_at"]
        depth = 1
