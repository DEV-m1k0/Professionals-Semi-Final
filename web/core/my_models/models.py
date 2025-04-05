from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class MarkMachine(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class ModelMachine(models.Model):
    title = models.CharField(max_length=255)
    mark_machine = models.ForeignKey("MarkMachine", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return self.title
    
    
class MachineTypePaymentMethod(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MachineWorkStatus(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class VendingMachine(models.Model):
    address = models.CharField(max_length=255)
    model = models.ForeignKey("ModelMachine", on_delete=models.SET_NULL, null=True)
    type = models.ForeignKey("MachineTypePaymentMethod", on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey("MachineWorkStatus", on_delete=models.SET_NULL, null=True)
    date_of_instalation = models.DateField()
    date_of_service = models.DateField()
    all_income = models.BigIntegerField()

    def __str__(self) -> str:
        return f"Вендинговая машина pk={self.pk} address={self.address}"


class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    price = models.BigIntegerField()
    amount = models.BigIntegerField()
    min_amount = models.BigIntegerField()
    frequency_of_purchases = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title
    

class PurcheseMethod(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Purchese(models.Model):
    machine = models.ForeignKey("VendingMachine", on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey("Product", on_delete=models.SET_NULL, null=True)
    amount = models.BigIntegerField()
    earned = models.BigIntegerField()
    created_date = models.DateTimeField(auto_created=True)
    purchese_method = models.ForeignKey("PurcheseMethod", on_delete=models.SET_NULL, null=True)

    def __str__(self) -> str:
        return f"Продано {self.product} через {self.machine} в количестве {self.amount}. Получено {self.earned}"


class UserRole(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class MyUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    role = models.ForeignKey("UserRole", on_delete=models.SET_NULL, null=True)


class Service(models.Model):
    machine = models.ForeignKey("VendingMachine", on_delete=models.SET_NULL, null=True)
    date_of_service = models.DateField()
    work_description = models.TextField(max_length=255)
    problems = models.TextField(max_length=255, null=True, blank=True)
    worker = models.ForeignKey("MyUser", on_delete=models.SET_NULL, null=True)
