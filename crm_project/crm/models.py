# crm/models.py

from django.db import models

class Guest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    member = models.BooleanField(default=False)
    location = models.CharField(max_length=100)
    num_of_guests = models.IntegerField()
    table_no = models.CharField(max_length=10)
    bar_or_restaurant = models.CharField(max_length=15)
    date_time = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
