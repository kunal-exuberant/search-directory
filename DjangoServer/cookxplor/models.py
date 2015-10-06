from django.db import models

# Create your models here.

class Languages(models.Model):
    language_name = models.CharField(max_length=100)
    class Meta:
        db_table = 'languages'


class Locations(models.Model):
    location_name = models.CharField(max_length=100)
    state_name = models.CharField(max_length=100)
    pincode = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'location'

class Cusines(models.Model):
    cuisine_name = models.CharField(max_length=100)

    class Meta:
        db_table = 'cuisine'

class Timings(models.Model):
    start_time = models.IntegerField()
    end_time = models.IntegerField()

    class Meta:
        db_table = 'timings'

class Vendor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    contact_no = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100, blank=True, null=True)
    FOOD_TYPE_CHOICES = (
        (1, 'Veg'),
        (2, 'Non-Veg'),
        (3,'Both')
        )
    total_experience = models.FloatField(blank=True,null=True)
    address = models.CharField(max_length=100,null = True,blank=True)
    foodtype = models.CharField(max_length=10,choices=FOOD_TYPE_CHOICES,default=3)
    verification = models.BooleanField()
    chargespermonth = models.FloatField(blank=True, null=True)
    picture_path = models.CharField(max_length=1500,blank=True,null=True)
    date_of_birth = models.DateField()
    is_available_as_guest_cook = models.BooleanField()
    languages = models.ManyToManyField(Languages)
    locations = models.ManyToManyField(Locations)
    cusines = models.ManyToManyField(Cusines)
    timings = models.ManyToManyField(Timings)
    created_date = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'vendor'


class Charges(models.Model):
    min_charge = models.DecimalField(max_digits=6, decimal_places=2)
    min_charge_People = models.IntegerField()
    max_People = models.IntegerField()
    average_charge_per_Person = models.DecimalField(max_digits=6,decimal_places=2)
    vendor = models.OneToOneField(Vendor)

    class Meta:
        db_table = 'charges'
