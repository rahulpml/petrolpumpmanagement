from django.contrib import admin
from .models import Fueltype, Fuel, Machine, Tanker , Supplier ,Customer , Item ,Order, \
    OrderItem ,ShippingAddress , ServiceStation, Vehicle, Service ,FuelVehicle,FuelServiceStation,FuelService ,profilepic

# Register your models here.
admin.site.register(Fueltype)
admin.site.register(Fuel)
admin.site.register(Machine)
admin.site.register(Tanker)
admin.site.register(Supplier)
admin.site.register(Customer)

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(ServiceStation)
admin.site.register(Vehicle)
admin.site.register(Service)
admin.site.register(FuelServiceStation)
admin.site.register(FuelVehicle)
admin.site.register(FuelService)
admin.site.register(profilepic)