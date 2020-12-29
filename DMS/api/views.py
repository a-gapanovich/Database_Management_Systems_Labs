from rest_framework.viewsets import ModelViewSet
from api.serializers import (
    ProductLinesSerializer,
    OrderDetailsSerializer,
    CustomersSerializer,
    EmployeesSerializer,
    PaymentsSerializer,
    ProductsSerializer,
    OfficesSerializer,
    OrdersSerializer
)
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


# Create your views here.
class ProductLinesView(ModelViewSet):
    serializer_class = ProductLinesSerializer
    queryset = ProductLines.objects.all()


class OrderDetailsView(ModelViewSet):
    serializer_class = OrderDetailsSerializer
    queryset = OrderDetails.objects.all()


class CustomersView(ModelViewSet):
    serializer_class = CustomersSerializer
    queryset = Customers.objects.all()


class EmployeesView(ModelViewSet):
    serializer_class = EmployeesSerializer
    queryset = Employees.objects.all()


class PaymentsView(ModelViewSet):
    serializer_class = PaymentsSerializer
    queryset = Payments.objects.all()


class ProductsView(ModelViewSet):
    serializer_class = ProductsSerializer
    queryset = Products.objects.all()


class OfficesView(ModelViewSet):
    serializer_class = OfficesSerializer
    #queryset = Offices.objects.all()
    queryset = Offices.objects.exclude(country = 'USA')


class OrdersView(ModelViewSet):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()