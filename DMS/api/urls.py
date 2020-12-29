from django.urls import path
from api.views import (
    OrderDetailsView,
    ProductLinesView,
    EmployeesView,
    CustomersView,
    PaymentsView,
    ProductsView,
    OfficesView,
    OrdersView,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"order-details", OrderDetailsView)
router.register(r"product-lines", ProductLinesView)
router.register(r"employees", EmployeesView)
router.register(r"customers", CustomersView)
router.register(r"payments", PaymentsView)
router.register(r"products", ProductsView)
router.register(r"offices", OfficesView)
router.register(r"orders", OrdersView)

urlpatterns = router.urls