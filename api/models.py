from django.db import models

class Friend(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Expense(models.Model):
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    friend = models.ForeignKey(Friend, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.description} - ${self.amount}"