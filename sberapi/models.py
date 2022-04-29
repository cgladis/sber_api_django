import datetime

from django.db import models

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    user = models.CharField(max_length=100)
    account_id = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.name


class ClientData(models.Model):
    PAYMENTS = 'payments'
    CHARGES = 'charges'
    MEASUREMENTS = 'measurements'
    TYPE_CHOICES = [(PAYMENTS, 'payments'),
                    (CHARGES, 'charges'),
                    (MEASUREMENTS, 'measurements')]
    account_id = models.CharField(max_length=20)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    dt = models.DateTimeField(default=datetime.datetime.now)
    sum = models.IntegerField()

    def __str__(self):
        return f'{self.dt:%d.%m.%Y %H:%M} : {self.account_id} : {self.type} / {self.sum}'
