from django.contrib import admin
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


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("productName", "productCode", "productLine")


class OrdersAdmin(admin.ModelAdmin):
    list_display = ("orderNumber", "status",)


class OrderDetailsAdmin(admin.ModelAdmin):
    list_display = ("productCode", "orderNumber", "quantityOrdered")


class OfficesAdmin(admin.ModelAdmin):
    list_display = ("officeCode", "country", "postalCode")


class CustomersAdmin(admin.ModelAdmin):
    list_display = ("customerName", "customerNumber", "phone", "country")


class PaymentsAdmin(admin.ModelAdmin):
    list_display = ("checkNumber", "customerNumber", "amount",)


admin.site.register(ProductLines)
admin.site.register(OrderDetails, OrderDetailsAdmin)
admin.site.register(Customers, CustomersAdmin)
admin.site.register(Employees)
admin.site.register(Payments, PaymentsAdmin)
admin.site.register(Products, ProductsAdmin)
admin.site.register(Offices, OfficesAdmin)
admin.site.register(Orders, OrdersAdmin)