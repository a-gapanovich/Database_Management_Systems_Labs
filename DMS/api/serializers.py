from rest_framework import serializers
from app.models import (
    ProductLines,
    OrderDetails,
    Customers,
    Employees,
    Payments,
    Products,
    Offices,
    Orders,
)


class ProductLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductLines
        fields = "__all__"


class OrderDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetails
        fields = "__all__"


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = "__all__"


class EmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = "__all__"


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = "__all__"


class OfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offices
        #fields = "__all__"
        fields = ("postalCode", "phone")


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = "__all__"