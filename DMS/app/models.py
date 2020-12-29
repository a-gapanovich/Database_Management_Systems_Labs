from django.db import models
from django.utils.timezone import now


# Create your models here.
class Customers(models.Model):
    customerNumber = models.IntegerField("Customer Number")
    customerName = models.CharField("Customer Name", max_length=50)
    contactLastName = models.CharField("Contact Last Name", max_length=50)
    contactFirstName = models.CharField("Contact First Name", max_length=50)
    phone = models.CharField("Phone", max_length=50)
    addressLine1 = models.CharField("Address Line 1", max_length=50)
    addressLine2 = models.CharField("Address Line 2", max_length=50, blank=True, null=True, default=None)
    city = models.CharField("City", max_length=50)
    state = models.CharField("State", max_length=50, blank=True, null=True, default=None)
    postalCode = models.CharField("Postal Code", max_length=15, blank=True, null=True, default=None)
    country = models.CharField("Country", max_length=30)
    salesRepEmployeeNumber = models.IntegerField(
        "Sales Employee Number",
        default=None,
        blank=True,
        null=True
    )
    creditLimit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=None)

    def __str__(self):
        return self.customerName


class Employees(models.Model):
    employeeNumber = models.IntegerField("Employee Number")
    lastName = models.CharField("Last Name", max_length=50)
    firstName = models.CharField("First Name", max_length=50)
    extension = models.CharField("Extension", max_length=10)
    email = models.EmailField("Email", max_length=100)
    officeCode = models.CharField("Office Code", max_length=10)
    reportsTo = models.IntegerField("Report to", blank=True, null=True, default=None)
    jobTitle = models.CharField("Job Title", max_length=50)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class Offices(models.Model):
    officeCode = models.CharField("Office Code", max_length=10)
    city = models.CharField("City", max_length=50)
    phone = models.CharField("Phone", max_length=50)
    addressLine1 = models.CharField("Address Line 1", max_length=50)
    addressLine2 = models.CharField("Address Line 2", max_length=50, blank=True, null=True, default=None)
    state = models.CharField("State", max_length=50, blank=True, null=True, default=None)
    country = models.CharField("Country", max_length=30)
    postalCode = models.CharField("Postal Code", max_length=15)
    territory = models.CharField("Territory", max_length=10)

    def __str__(self):
        return self.officeCode


class OrderDetails(models.Model):
    orderNumber = models.IntegerField("Order Number")
    productCode = models.CharField("Product Code", max_length=15)
    quantityOrdered = models.IntegerField("Quantity Ordered")
    priceEach = models.DecimalField("Price Each", max_digits=10, decimal_places=2)
    orderLineNumber = models.SmallIntegerField("Order Line Number")

    def __str__(self):
        return self.productCode


class Orders(models.Model):
    orderNumber = models.IntegerField("Order Number")
    orderDate = models.DateField("Order Date", default=now())
    requiredDate = models.DateField("Required Date", default=now())
    shippedDate = models.DateField("Shipped Date", default=None, blank=True, null=True)
    status = models.CharField("Status", max_length=15)
    comments = models.TextField("Comments", blank=True, null=True, default=None)
    customerNumber = models.IntegerField("Customer Number")

    def __str__(self):
        return str(self.orderNumber)


class Payments(models.Model):
    customerNumber = models.IntegerField("Customer Number")
    checkNumber = models.CharField("Check Number", max_length=50)
    paymentDate = models.DateField("Payment Date", default=now())
    amount = models.DecimalField("Amount", max_digits=10, decimal_places=2)

    def __str__(self):
        return self.checkNumber


class ProductLines(models.Model):
    productLine = models.CharField("Product Line", max_length=50)
    textDescription = models.CharField("Text Description", max_length=4000)
    htmlDescription = models.TextField("HTML Description", default=None, blank=True, null=True)
    image = models.ImageField("Image", default=None, blank=True, null=True)

    def __str__(self):
        return self.productLine


class Products(models.Model):
    productCode = models.CharField("Product Code", max_length=15)
    productName = models.CharField("Product Name", max_length=70)
    productLine = models.CharField("Product Line", max_length=50)
    productScale = models.CharField("Product Scale", max_length=10)
    productVendor = models.CharField("Product Vendor", max_length=50)
    productDescription = models.TextField("Product Description")
    quantityInStock = models.SmallIntegerField("Quantity In Stock")
    buyPrice = models.DecimalField("Buy Price", max_digits=10, decimal_places=2)
    MSRP = models.DecimalField("MSRP", max_digits=10, decimal_places=2)



