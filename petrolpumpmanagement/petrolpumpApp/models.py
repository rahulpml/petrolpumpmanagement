from django.db import models

from django.contrib.auth.models import User

# Create your models here.



#Customer model
class Customer(models.Model):
    cust_id = models.OneToOneField(to=User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    cust_phone = models.CharField(max_length=12)
    address = models.CharField(max_length = 100)


    def __str__(self):
        return self.first_name + " " + self.last_name




#Ouery helper
class BookinQuerySet(models.QuerySet):
    def bookings(self, owner=None):
        if owner:
            return self.filter(owner=owner)
        return self
class ServiceQuerySet(models.QuerySet):
    def services(self, ss=None):
        if ss:
            return self.filter(ss=ss)
        return self


#Vehicle Manager
class VehicleManager(models.Manager):
    def create_vehicle(self,vehicle_reg_no,vehicle_name,vehicle_type,owner):
        return self.create(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=owner)
    def get_queryset(self):
        return BookinQuerySet(self.model,using=self._db)
    def bookings(self,owner=None):
        if owner:
            return self.get_queryset().bookings(owner=owner)
        return self.get_queryset().bookings()


#Service Manager
class ServiceManager(models.Manager):
    def create_service(self,veh,type_of_service,service_desc,ser_status,ss):
        return self.create(veh=veh,type_of_service=type_of_service,service_desc=service_desc,ser_status=ser_status,ss=ss)
    def get_queryset(self):
        return ServiceQuerySet(self.model,using=self._db)
    def services(self,ss=None):
        if ss:
            return self.get_queryset().services(ss=ss)
        return self.get_queryset().services()



# ServiceStation model
class ServiceStation(models.Model):
    stat_id = models.OneToOneField(to=User,on_delete=models.CASCADE)  
    station_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100)
    ss_phone = models.CharField(max_length=12)

    def __str__(self): 
        return self.station_name




    #Vehicle model
class Vehicle(models.Model):
    vehicle_reg_no = models.CharField(max_length=10)
    vehicle_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=20)
    owner = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    objects = VehicleManager()

    def __str__(self): 
        return self.vehicle_name



#Service model
class Service(models.Model):
    service_status = (('Waiting','Waiting'),('In progress','In progress'),('Completed','Completed'))
    ss = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    ser = models.ForeignKey(to=ServiceStation,on_delete=models.CASCADE,null=True)
    veh = models.OneToOneField(to=Vehicle,on_delete=models.CASCADE,null=True)
    type_of_service = models.CharField(max_length=50,null=True)
    service_desc = models.CharField(max_length=1000,null=True)
    ser_status = models.CharField(max_length=100,choices=service_status,null=True)
    start_date = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField(null=True)
    objects = ServiceManager()

    def __str__(self): 
        return self.ss

#supplier
class Supplier(models.Model): 
    name = models.CharField(max_length=250)
    email = models.EmailField() 
    phone = models.CharField(max_length=12)

    def __str__(self): 
        return self.name 

#fueltype 
  
class Fueltype(models.Model):
    fueltype = models.CharField(max_length=255)
    
    def __str__(self): 
        return self.fueltype
#fuel

class Fuel(models.Model):
    fueltype = models.ForeignKey(Fueltype, on_delete=models.CASCADE , null=True)
    price = models.IntegerField()

 
   

class Machine(models.Model):
    fueltype = models.ForeignKey(Fueltype, on_delete=models.SET_NULL , null=True)
    machine_no = models.IntegerField()
    company_name = models.CharField(max_length=255)
    machine_des = models.TextField()

class Tanker(models.Model):
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    fueltype = models.ForeignKey(Fueltype, on_delete=models.SET_NULL , null=True)
    tanker_no = models.IntegerField()
    tanker_date = models.DateField()
    quantity = models.IntegerField()
    tanker_des = models.TextField()

    def __str__(self):
        return str(self.id)


#admincustomer
class admincustomer(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    supplier=models.ForeignKey(Supplier, on_delete=models.SET_NULL,blank=True, null=True)
    tanker = models.ForeignKey(Tanker, on_delete=models.SET_NULL, blank=True, null=True)
    fueltype = models.ForeignKey(Fueltype, on_delete=models.SET_NULL , null=True)
    fuelquantity = models.IntegerField(null=True, blank=True, default=0,)
    remarks = models.TextField(blank=True, null=True, )    


#Vehicle Manager
class VehicleManager1(models.Manager):
    def create_vehicle1(self,vehicle_reg_no,vehicle_name,vehicle_type,owner):
        return self.create(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=owner)
    def get_queryset(self):
        return BookinQuerySet(self.model,using=self._db)
    def bookings(self,owner=None):
        if owner:
            return self.get_queryset().bookings(owner=owner)
        return self.get_queryset().bookings()

class ServiceManager1(models.Manager):
    def create_service1(self,veh,type_of_fuel,fuel_qua,ser_status,ss):
        return self.create(veh=veh,type_of_fuel=type_of_fuel,fuel_qua=fuel_qua,ser_status=ser_status,ss=ss)
    def get_queryset(self):
        return ServiceQuerySet(self.model,using=self._db)
    def services(self,ss=None):
        if ss:
            return self.get_queryset().services(ss=ss)
        return self.get_queryset().services()        

#Vehicle model
class FuelVehicle(models.Model):
    vehicle_reg_no = models.CharField(max_length=10)
    vehicle_name = models.CharField(max_length=50)
    vehicle_type = models.CharField(max_length=10000)
    owner = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    objects = VehicleManager1()


    def __str__(self): 
        return self.vehicle_name

    
class FuelServiceStation(models.Model):
    stat_id = models.OneToOneField(to=User,on_delete=models.CASCADE)  
    station_name = models.CharField(max_length=100,default='')
    email = models.CharField(max_length=100,default='')
    address = models.CharField(max_length=100)
    ss_phone = models.CharField(max_length=12)

    def __str__(self): 
        return self.station_name

#Service model
class FuelService(models.Model):
    service_status = (('Waiting','Waiting'),('In progress','In progress'),('Completed','Completed'))
    ss = models.ForeignKey(to=Customer,on_delete=models.CASCADE)
    ser = models.ForeignKey(to=FuelServiceStation,on_delete=models.CASCADE,null=True)
    veh = models.ForeignKey(to=FuelVehicle,on_delete=models.CASCADE,null=True)
    type_of_fuel = models.CharField(max_length=100,null=True)
    fuel_qua = models.IntegerField(default=1)
    ser_status = models.CharField(max_length=100,choices=service_status,null=True)
    start_date = models.DateTimeField(auto_now=True)
    finish_date = models.DateTimeField(null=True)
    objects = ServiceManager1() 

    def __str__(self): 
        return self.ss

   


#ecart




CATEGORY_CHOICES = (
    ('P', 'Parts'),
    ('E', 'Engine'),
    ('O', 'Oil')
)


class Item(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Order(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField
    ordered = models.BooleanField(default=False)
    transaction_id = models.BooleanField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

class OrderItem(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    item = models.ForeignKey(Item, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    def __str__(self):
        return self.item.name        

class ShippingAddress(models.Model):
    username = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    road_no = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

#avatar = models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)


class profilepic(models.Model):
    avatar = models.ImageField(upload_to='profile_pic/CustomerProfilePic/',null=True,blank=True)