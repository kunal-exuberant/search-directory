from django.db import models

# Create your models here.

class Vendor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=100)
    FOOD_TYPE_CHOICES = (
        (1, 'Veg'),
        (2, 'Non-Veg'),
        (3,'Both')
        )
    foodtype = models.CharField(max_length=10,choices=FOOD_TYPE_CHOICES,default=3)
    verification = models.BooleanField()
    chargespermonth = models.FloatField(blank=True, null=True)

    class Meta:
        db_table = 'vendor'


class Languages(models.Model):
    language_name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor)
    class Meta:
        db_table = 'languages'


class Location(models.Model):
    location_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    pincode = models.IntegerField(blank=True, null=True)
    vendor = models.ForeignKey(Vendor)

    class Meta:
        db_table = 'location'

class Cusine(models.Model):
    cuisine_name = models.CharField(max_length=100)
    vendor = models.ForeignKey(Vendor)

    class Meta:
        db_table = 'cuisine'

class Timings(models.Model):
    start_time = models.DateField()
    end_time = models.DateField()
    vendor = models.ForeignKey(Vendor)

    class Meta:
        db_table = 'timings'


class Charges(models.Model):
    min_charge = models.DecimalField(max_digits=6, decimal_places=2)
    min_charge_People = models.IntegerField()
    max_People = models.IntegerField()
    average_charge_per_Person = models.DecimalField(max_digits=6,decimal_places=2)
    vendor = models.ForeignKey(Vendor)

    class Meta:
        db_table = 'charges'
