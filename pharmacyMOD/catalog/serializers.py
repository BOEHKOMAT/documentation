from rest_framework import serializers
from .models import Medicine, User, Order


class MedicineSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, required=True)
    quantity = serializers.CharField(max_length=10)
    price = serializers.CharField(max_length=10, required=True)
    description = serializers.CharField(max_length=1000)

    def create(self, validated_data):
        return Medicine.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=32, required=True)
    provisor_status = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.provisor_status = validated_data.get('provisor_status', instance.provisor_status)
        instance.save()
        return instance


class OrderSerializer(serializers.Serializer):
    user = UserSerializer()

    class Meta:
        model = Order
        fields = ['user', 'list']
    # list = serializers.CharField(max_length=500, required=True)

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        order = Order.objects.create(**validated_data)
        User.objects.create(order=order, **user_data)
        return order
