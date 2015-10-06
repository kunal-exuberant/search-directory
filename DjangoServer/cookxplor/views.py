from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Vendor,Languages,Locations,Cusines,Timings,Charges
import sys
import json

# Create your views here.
@csrf_exempt
def register(request):
    try:
        if request.method=='POST':
            #reader = codecs.getreader("utf-8")
            vendordetail = json.loads(request.body.decode("utf-8"))
            vendor = Vendor(first_name=vendordetail['firstname'],last_name = vendordetail['lastname'],contact_no= vendordetail['mobile'],email_id = vendordetail['email_id'],total_experience=vendordetail['total_experience'],address = vendordetail['address'],foodtype=vendordetail['food_type'],verification=True if vendordetail['verification']=='true' else False,chargespermonth=0.0,picture_path=vendordetail['picture_path'],date_of_birth=vendordetail['DOB'],is_available_as_guest_cook = vendordetail['isAvailableasGuestCook'])
            vendor.save()
            for location in vendordetail['service_area']:
                templocation = Locations.objects.create(location_name=location,state_name='Karnataka',pincode='560048')
                vendor.locations.add(templocation)
            for cuisine in vendordetail['food_variety']:
                tempcuisine = Cusines.objects.create(cuisine_name = cuisine)
                vendor.cusines.add(tempcuisine)
            #timings=json.loads(vendordetail['available_timing'])
            for timing in vendordetail['available_timing']:
                temptiming = Timings.objects.create(start_time = timing['startTime'],end_time=timing['endTime'])
                vendor.timings.add(temptiming)
            #charges = json.loads(vendordetail['charges'])
            #for charge in charges:
            charges = Charges(vendor = vendor,min_charge=vendordetail['charges']['min_charge'],min_charge_People=vendordetail['charges']['min_charge_people'],max_People=vendordetail['charges']['max_people'],average_charge_per_Person=vendordetail['charges']['average_charge_per_person'])
           # vendor.charges.create(min_charge=charge['min_charge'],min_charge_people=charge['min_charge_people'],max_people=charge['max_people'],average_charge_per_person=charge['average_charge_per_person'])
            charges.save()
            #vendor.save()
            #request.Body
            #print("I am at register")
            return HttpResponse('OK')
        elif request.method=='GET':
            return HttpResponse('sahi pakde ho')
        else:
            return HttpResponse("Unknown")
    except:
         return HttpResponse(sys.exc_info())
        
        
