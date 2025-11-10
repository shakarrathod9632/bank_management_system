from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
            return True
        return False

    def __str__(self):
        return f"{self.name} - {self.account_number}"

