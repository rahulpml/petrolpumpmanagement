from django.shortcuts import render ,redirect ,reverse
from django.contrib import messages
from django.db import connection
from django.contrib.auth import authenticate , logout 
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from .models import admincustomer ,Item ,Customer , ServiceStation ,Vehicle , Service ,Supplier , Fueltype,Fuel , Machine ,Tanker , FuelVehicle , FuelService
from .forms import (updateservice ,updatefuel ,AdmincustomerForm ,FuelBooking ,TankerForm ,MachineForm,FuelForm,FueltypeForm,SupplierForm,CustomerRegistrationForm,
CustomerInfoForm,ServiceStationRegistrationForm,ServiceStationInfoForm,CustomerLoginForm,ServiceStationLoginForm,VBooking)
from django.contrib.auth.decorators import login_required
from .import models

# Create your views here.


def home(request):
    return render(request,'home.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')

def customer_register(request):
    cus_form = CustomerRegistrationForm()
    cus_info_form = CustomerInfoForm()

    if request.method == 'POST':
        cus_form = CustomerRegistrationForm(request.POST)
        cus_info_form = CustomerInfoForm(request.POST)
        if cus_form.is_valid() and cus_info_form.is_valid():
            username = cus_form.cleaned_data['username']
            first_name = cus_info_form.cleaned_data['first_name']
            last_name = cus_info_form.cleaned_data['last_name']
            email = cus_info_form.cleaned_data['email']
            cust_phone = cus_info_form.cleaned_data['cust_phone']
            address = cus_info_form.cleaned_data['address']
            if cus_form.cleaned_data['password'] == cus_form.cleaned_data['password_confirm']:
                new_cust = User.objects.create(
                   username=username,
                   is_superuser=False
                )
                new_cust.set_password(cus_form.cleaned_data['password'])
                new_cust.save()
                new_cus_info = Customer()
                new_cus_info.cust_id = new_cust
                new_cus_info.first_name = first_name
                new_cus_info.last_name = last_name
                new_cus_info.email = email
                new_cus_info.address = address
                new_cus_info.cust_phone = cust_phone
                new_cus_info.save()
                
                
                return redirect('home')
        else:
            cus_form = CustomerRegistrationForm()
            cus_info_form = CustomerInfoForm()
    context = {
        'cus_form': cus_form,
        'cus_info_form': cus_info_form
    }
    return render(request,'customer_reg.html',context)


def service_register(request):
    ser_form = ServiceStationRegistrationForm()
    ser_info_form = ServiceStationInfoForm()
    if request.method == 'POST':
         ser_form = ServiceStationRegistrationForm(request.POST)
         ser_info_form = ServiceStationInfoForm(request.POST)
         if ser_form.is_valid() and ser_info_form.is_valid():
             username = ser_form.cleaned_data['username']
             station_name = ser_info_form.cleaned_data['station_name']
             email = ser_info_form.cleaned_data['email']
             ss_phone = ser_info_form.cleaned_data['ss_phone']
             address = ser_info_form.cleaned_data['address']
             if ser_form.cleaned_data['password'] == ser_form.cleaned_data['password_confirm']:
                 if User.objects.filter(username=username).exists():
                     messages.info(request,'Username Taken..')
                 elif User.objects.filter(email=email).exists():
                     messages.info(request,'Email Taken..')
                 else:
                    new_ser = User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=ser_form.cleaned_data['password'],
                    is_superuser=True
                    )
                 new_ser.save()
                 new_ser_info = ServiceStation()
                 new_ser_info.station_name = station_name
                 new_ser_info.stat_id = new_ser
                 new_ser_info.email = email
                 new_ser_info.address = address
                 new_ser_info.ss_phone = ss_phone
                 new_ser_info.save()
                 return redirect('home')                 
             else:
                 messages.info(request,'Password not matching')

             ser_form = ServiceStationRegistrationForm()
             ser_info_form = ServiceStationInfoForm()
    context = {
        'ser_form': ser_form,
        'ser_info_form': ser_info_form
    }
    return render(request,'service_reg.html',context)    

#login

def customer_login(request):
    cust_log = CustomerLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_superuser :
                request.session['uname'] = username
                auth.login(request, user)
                return redirect('admindashboard-view')

            else :
                request.session['uname'] = username
                auth.login(request,user)
                return redirect('customerdashboard-view')
                
    else:
        
        context = {
                 'cust_log':cust_log,
                 }
        return render(request,'customer_log.html',context)
    msg = 'oops ...! Create your profile first'       
    context = {
        'cust_log': cust_log ,
        'msg':msg
    }

    return render(request, 'customer_log.html', context)

#####################333

def service_login(request):
    ser_log = ServiceStationLoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser == True:
                if user.is_active:
                    auth.login(request, user)
                    return redirect('admindashboard-view')
                
        else:
             msg = 'Username or Password Incorect '
             context = {
                'ser_log':ser_log,
                'msg':msg}
             return render(request,'service_log.html',context)
                
    context = {
        'ser_log': ser_log,
    }
    return render(request, 'service_log.html', context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


#customer dashboard view
def cust_dash(request):
    return render(request,'cust_dash.html')  


def cust_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {
        'user':user
    }
    return render(request,'cust_profile.html',context)    

#service cemter dashboard view
def ser_dash(request):
    return render(request,'ser_dash.html')

def ser_profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    context = {
        'user':user
    }
    return render(request,'ser_profile.html',context)

def booking(request):
    form = VBooking()
    if request.method == 'POST':
        form = VBooking(request.POST)
        if form.is_valid():
            cust = request.user.customer
            cust.save()
            vehicle_reg_no = form.cleaned_data['vehicle_reg_no']
            vehicle_name = form.cleaned_data['vehicle_name']
            vehicle_type = form.cleaned_data['vehicle_type']
            type_of_service = form.cleaned_data['type_of_service']
            service_desc = form.cleaned_data['service_desc']
            ser_status = 'Waiting'
            v = Vehicle.objects.create_vehicle(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=cust)
            v.save()
            s = Service.objects.create_service(veh=v,type_of_service=type_of_service,service_desc=service_desc,ser_status=ser_status,ss=cust)
            s.save()
            return redirect('bookings-view')
    else:
        form = VBooking()
    context = {
        'form':form
    }
    return render(request,'create_booking.html',context)        


#bookings view for customer 
def bookings_view(request):
        cust = request.user.customer
        booking_list = Vehicle.objects.bookings(cust)
        service_list = Service.objects.services(cust)
        context = {
            'booking_list': booking_list,
            'service_list': service_list
        }
        return render(request,'bookings_view.html',context)


# service view for service station
def service_view(request):
    ser = Service.objects.all()
    context = {
        'ser': ser
    }
    return render(request,'service_view.html',context)

#delete service bookings
def deleteservice_view(request,id):
    deleteService = Service.objects.get(id=id)
    deleteVehicle = Vehicle.objects.get(id=id)
    deleteService.delete()
    deleteVehicle.delete()
    return redirect('service-view')

###delete fuel bookings

# status udpattion procedure call for updating status of service 
def udpate_status(request):
    if request.method == 'POST':
        service_id = int(request.POST['service_id'])
        status = request.POST['status']
        cursor = connection.cursor()
        cursor.execute("call update_status(%s,%s)",(service_id,status))
        return redirect('service-view')
    return render(request,'update_status.html')            
#serviceupdatestatus
def updateservice_view(request , id):
    ser = Service.objects.filter(id=id).first()
    form = updateservice(request.POST , instance=ser)
    if form.is_valid() :
        form.save()
        return redirect('service-view')
    context = {
        'form':form ,
        'ser':ser
    }
    return render(request,'updateservice.html', context)  

# HomeView
def Supplier_view(request): 
    suppliers = Supplier.objects.all()
    form = SupplierForm()
    context = {
        'suppliers': suppliers, 
        'form':form, 
    }
    return render(request, 'Supplier_view.html', context)

# InsertView
def addSupplier(request): 
    if request.method == 'POST': 
        form = SupplierForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('homesupplier')

# EditView
def editSupplier(request,id): 
    select = Supplier.objects.get(id=id)
    form = SupplierForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('homesupplier') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteSupplier(request, id): 
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('homesupplier')



#addfueltype

def Fueltype_view(request): 
    fueltypes = Fueltype.objects.all()
    form = FueltypeForm()
    context = {
        'fueltypes': fueltypes, 
        'form':form, 
    }
    return render(request, 'Fueltype_view.html', context)

#InsertView
def addFueltype(request): 
    if request.method == 'POST': 
        form = FueltypeForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home1')

# EditView
def editFueltype(request,id): 
    select = Fueltype.objects.get(id=id)
    form = FueltypeForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home1') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteFueltype(request, id): 
    supplier = Fueltype.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home1')



#addfuel



#addfueltype

def Fuel_view(request): 
    fuels = Fuel.objects.all()
    form = FuelForm()
    context = {
        'fuels': fuels, 
        'form':form, 
    }
    return render(request, 'Fuel_view.html', context)

#InsertView
def addFuel(request): 
    if request.method == 'POST': 
        form = FuelForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home2')

# EditView
def editFuel(request,id): 
    select = Fuel.objects.get(id=id)
    form = FuelForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home2') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteFuel(request, id): 
    supplier = Fuel.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home2')


#addmachine

def Machine_view(request): 
    machines = Machine.objects.all()
    form = MachineForm()
    context = {
        'machines': machines, 
        'form':form, 
    }
    return render(request, 'Machine_view.html', context)




#InsertView
def addMachine(request): 
    if request.method == 'POST': 
        form = MachineForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home3')

# EditView
def editMachine(request,id): 
    select = Machine.objects.get(id=id)
    form = MachineForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home3') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteMachine(request, id): 
    supplier = Machine.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home3')


#addTanker


def Tanker_view(request): 
    tankers = Tanker.objects.all()
    form = TankerForm()
    context = {
        'tankers': tankers, 
        'form':form, 
    }
    return render(request, 'Tanker_view.html', context)

#InsertView
def addTanker(request): 
    if request.method == 'POST': 
        form = TankerForm(request.POST or None)
        if form.is_valid(): 
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home4')

# EditView
def editTanker(request,id): 
    select = Tanker.objects.get(id=id)
    form = TankerForm(request.POST or None, instance=select) 
    if request.method == 'POST':
        if form.is_valid(): 
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home4') 
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteTanker(request, id): 
    supplier = Tanker.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home4')

#admincustomer
def admincustomer_view(request):
    tankers = admincustomer.objects.all()
    form = AdmincustomerForm()
    context = {
        'tankers': tankers,
        'form':form,
    }
    return render(request, 'admincustomer_view.html', context)
#InsertView
def addadmincustomerview(request):
    if request.method == 'POST':
        form = AdmincustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your information has been inserted!')
            return redirect('home5')

# EditView
def editadmincustomerview(request,id):
    select = admincustomer.objects.get(id=id)
    form = AdmincustomerForm(request.POST or None, instance=select)
    if request.method == 'POST':
        if form.is_valid():
            dev = form.save(commit=False)
            dev.save()
            messages.success(request, f'Data has been updated!')
            return redirect('home5')
    # return render(request, 'myapp/edit.html',{'form':form})


# DeleteView
def deleteadmincustomerview(request, id):
    supplier = admincustomer.objects.get(id=id)
    supplier.delete()
    messages.success(request, f'Data has been deleted!')
    return redirect('home5')

# ====


def fuelbooking(request):
    form = FuelBooking()
    if request.method == 'POST':
        form = FuelBooking(request.POST)
        if form.is_valid():
            cust = request.user.customer
            cust.save()
            vehicle_reg_no = form.cleaned_data['vehicle_reg_no']
            vehicle_name = form.cleaned_data['vehicle_name']
            vehicle_type = form.cleaned_data['vehicle_type']
            type_of_fuel = form.cleaned_data['type_of_fuel']
            fuel_qua = form.cleaned_data['fuel_qua']
            ser_status = 'Waiting'
            v = FuelVehicle.objects.create_vehicle1(vehicle_reg_no=vehicle_reg_no,vehicle_name=vehicle_name,vehicle_type=vehicle_type,owner=cust)
            v.save()
            s = FuelService.objects.create_service1(veh=v,type_of_fuel=type_of_fuel,fuel_qua=fuel_qua,ser_status=ser_status,ss=cust)
            s.save()
            return redirect('fuelbookings-view')
    else:
        form = FuelBooking()
    context = {
        'form':form
    }
    return render(request,'create_fuelbooking.html',context)    


#bookings view for customer 
def fuelbookings_view(request):
        cust = request.user.customer
        booking_list = FuelVehicle.objects.bookings(cust)
        service_list = FuelService.objects.services(cust)
        context = {
            'booking_list': booking_list,
            'service_list': service_list
        }
        return render(request,'fuelbookings_view.html',context)

# service view for service station
def fuelservice_view(request):
    ser = FuelService.objects.all()
    context = {
        'ser': ser
    }
    return render(request,'fuelservice_view.html',context)

#delete fuel bookings
def deletefuelservice_view(request,id):
    deleteFuelService = FuelService.objects.get(id=id)
    deleteFuelVehicle = FuelVehicle.objects.get(id=id)
    deleteFuelService.delete()
    deleteFuelVehicle.delete()
    return redirect('fuelservice-view')



# status udpattion procedure call for updating status of service 
#def fuelupdate_status(request):
    #if request.method == 'POST':
        #service_id = int(request.POST['service_id'])
       # status = request.POST['status']
       # cursor = connection.cursor()
       # cursor.execute("call update_status(%s,%s)",(service_id,status))
       # return redirect('fuelservice-view')
   # return render(request,'fuelupdate_status.html')
#fuekupdatestatus
def updatefuel_view(request , id):
    ser = FuelService.objects.filter(id=id).first()
    form = updatefuel(request.POST , instance=ser)
    if form.is_valid() :
        form.save()
        return redirect('fuelservice-view')
    context = {
        'form':form ,
        'ser':ser
    }
    return render(request,'updatefuelservice.html', context)   




#################

def fuelavailable_view(request):
    tank = Tanker.objects.all()
    context = {
        'tank': tank
    }
    return render(request,'fuelavailable.html',context)
#def customersview(request):
   # customers = Customer.objects.all()
    #fuelvehicles = FuelVehicle.objects.all()
    #return render(request, 'customersview_view.html', {'customers':customers, 'fuelvehicles':fuelvehicles})


#def deletecustomersview(request, id): 
    #supplier = Customer.objects.get(id=id)
    #supplier.delete()
    #return redirect('customersview-view')

def totalcustomer_view(request):
    custm = Customer.objects.all()
    context = {
        'custm': custm
    }   
    return render(request,'customersview_view.html',context)

def delete_customer_view(request,id):
    supplier = models.User.objects.get(id=id)
    supplier.delete()
    return redirect('customersview-view')
#ecart


  #


def item_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "eStore/index.html", context)

def cart(request):
    context = {
    }
    return render(request, "eStore/cart.html", context)

@login_required(login_url='ser-log')
def admin_dashboard_view(request):
   

    return render(request,'admin_dashboard.html')   

@login_required(login_url='ser-log')
def customer_dashboard_view(request):
   

    return render(request,'customer_dashboard.html')  

def aboutus_view(request):
    return render(request,'aboutus.html')

 #contactus
 # 
def contactus_view(request):
    return render(request,'contactus.html')

#adminaddcustomer

def admincustomerregister(request):
    cus_form = CustomerRegistrationForm()
    cus_info_form = CustomerInfoForm()
    if request.method == 'POST':
        cus_form = CustomerRegistrationForm(request.POST)
        cus_info_form = CustomerInfoForm(request.POST)
        if cus_form.is_valid() and cus_info_form.is_valid():
            username = cus_form.cleaned_data['username']
            first_name = cus_info_form.cleaned_data['first_name']
            last_name = cus_info_form.cleaned_data['last_name']
            email = cus_info_form.cleaned_data['email']
            cust_phone = cus_info_form.cleaned_data['cust_phone']
            address = cus_info_form.cleaned_data['address']
            if cus_form.cleaned_data['password'] == cus_form.cleaned_data['password_confirm']:
                new_cust = User.objects.create(
                    username=username,
                    is_superuser=False
                )
                new_cust.set_password(cus_form.cleaned_data['password'])
                new_cust.save()
                new_cus_info = Customer()
                new_cus_info.cust_id = new_cust
                new_cus_info.first_name = first_name
                new_cus_info.last_name = last_name
                new_cus_info.email = email
                new_cus_info.address = address
                new_cus_info.cust_phone = cust_phone
                new_cus_info.save()

                return redirect('customersview-view')
        else:
            cus_form = CustomerRegistrationForm()
            cus_info_form = CustomerInfoForm()
    context = {
        'cus_form': cus_form,
        'cus_info_form': cus_info_form
    }
    return render(request, 'admincustomer_reg.html', context)