from rest_framework import serializers
from .models import Medicine, User, Order


class MedicineSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10, required=True)
    name = serializers.CharField(max_length=32, required=True)
    quantity = serializers.CharField(max_length=10)
    price = serializers.CharField(max_length=10, required=True)
    description = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Medicine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10, required=True)
    name = serializers.CharField(max_length=32, required=True)
    provisor_status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.provisor_status = validated_data.get('provisor_status', instance.provisor_status)
        instance.save()
        return instance


class OrderSerializer(serializers.Serializer):
    id = serializers.CharField(max_length=10, required=True)
    user_id = serializers.CharField(max_length=10, required=True)
    list = serializers.CharField(max_length=500, required=True)
    complete = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)
