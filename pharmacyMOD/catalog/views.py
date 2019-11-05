from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Medicine, User, Order
from .serializers import MedicineSerializer, UserSerializer, OrderSerializer


class MedicineView(APIView):
    def get(self, request, pk=None):
        medicines = Medicine.objects.all()
        serializer = MedicineSerializer(medicines, many=True)
        if pk is not None:
            return Response({"medicines": serializer.data[pk]})
        else:
            return Response({"medicines": serializer.data})

    def post(self, request):
        medicine = request.data.get('medicine')
        serializer = MedicineSerializer(data=medicine)
        if serializer.is_valid(raise_exception=True):
            medicine_saved = serializer.save()
        return Response({"success": "Medicine created successfully"})

    def put(self, request, pk):
        saved_medicine = get_object_or_404(Medicine.objects.all(), pk=pk)
        data = request.data.get('medicine')
        serializer = MedicineSerializer(instance=saved_medicine, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            medicine_saved = serializer.save()
        return Response({"success": "Medicine '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        medicine = get_object_or_404(Medicine.objects.all(), pk=pk)
        medicine.delete()
        return Response({"message": "Medicine with id `{}` has been deleted.".format(pk)}, status=204)


class UserView(APIView):
    def get(self, request, pk=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        if pk is not None:
            return Response({"users": serializer.data[pk]})
        else:
            return Response({"users": serializer.data})

    def post(self, request):
        user = request.data.get('user')
        serializer = UserSerializer(data=user)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User created successfully"})

    def put(self, request, pk):
        saved_user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data.get('user')
        serializer = UserSerializer(instance=saved_user, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "User '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        user = get_object_or_404(User.objects.all(), pk=pk)
        user.delete()
        return Response({"message": "User with id `{}` has been deleted.".format(pk)}, status=204)


class OrderView(APIView):
    def get(self, request, pk=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        if pk is not None:
            return Response({"orders": serializer.data[pk]})
        else:
            return Response({"orders": serializer.data})

    def post(self, request):
        order = request.data.get('order')
        serializer = OrderSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order created successfully"})

    def put(self, request, pk):
        saved_order = get_object_or_404(Order.objects.all(), pk=pk)
        data = request.data.get('order')
        serializer = OrderSerializer(instance=saved_order, data=data, partial=True)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order '{}' updated successfully".format(pk)})

    def delete(self, request, pk):
        order = get_object_or_404(Order.objects.all(), pk=pk)
        order.delete()
        return Response({"message": "Order with id `{}` has been deleted.".format(pk)}, status=204)
