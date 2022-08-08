from random import choices
from typing_extensions import Required

from django import forms
from django.forms import ModelForm
from .models import FuelService, Customer,ServiceStation,Service, Fueltype ,Supplier, Fueltype ,Fuel , Machine , Tanker , admincustomer , profilepic
from django.contrib.auth import get_user_model

#for User model
User = get_user_model

#CustomerRegistration form
class CustomerRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#CustomerInfo form
class CustomerInfoForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.TextInput())
    cust_phone = forms.CharField(widget=forms.TextInput(),label='Phone Number')
    address = forms.CharField(max_length=5000,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))


#ServiceStationRegistration form
class ServiceStationRegistrationForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(widget=forms.PasswordInput())

#ServiceStationInfo form
class ServiceStationInfoForm(forms.Form):
    station_name = forms.CharField(widget=forms.TextInput(), label='Fuel Station Name')
    email = forms.CharField(widget=forms.TextInput())
    ss_phone = forms.CharField(widget=forms.TextInput(),label='Phone Number')
    address = forms.CharField(max_length=5000,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

# CustomerLogin form
class CustomerLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#ServiceStationLogin form
class ServiceStationLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

#Booking form
class VBooking(forms.Form):
    choice = ( ('Two Wheel Vehicles','Two Wheel Vehicles'),
               ('Three Wheel Vehicles', 'Three Wheel Vehicles'),
               ('Car – Vehicles','Car – Vehicles'),
             ('Pick Up- Vehicles','Pick Up-Vehicles '),
                ('Bus – Road Vehicles','Bus – Road Vehicles'),
              ('Trucks – Vehicles','Trucks – Vehicles'),
              ('Backhoe – Heavy ','Backhoe – Heavy '),
              ('Tractor –  Vehicles','Tractor – Vehicles'))


    schoice = (('Wash','Wash'),
               ('Interim Service','Interim Service'),
               ('Denting','Denting'),
               ('Major Service','Major Service'),
               ('Full Service','Full Service'))

    vehicle_reg_no = forms.CharField(widget=forms.TextInput() ,label='Vehicle Registertaion Number')
    vehicle_name = forms.CharField(widget=forms.TextInput(), label='Vehicle Model')
    vehicle_type = forms.ChoiceField( choices=choice , label='Vehicle Type')
    type_of_service = forms.ChoiceField( choices=schoice ,label='Type of Service')
    service_desc = forms.CharField(max_length=5000,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}) , label='Service Description')


#updateservicestatus
class DateInput(forms.DateInput):
    input_type = 'date'

class updateservice(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['ss','ser_status','finish_date']
        widgets = {
            'finish_date': DateInput()
        }
############
#supplierform

class SupplierForm(forms.ModelForm): 
    class Meta: 
        model = Supplier
        fields = ['name', 'email', 'phone']


class FueltypeForm(forms.ModelForm): 
    class Meta: 
        model = Fueltype
        fields = ['fueltype']

class FuelForm(forms.ModelForm): 
    class Meta: 
        model = Fuel
        fields = ['fueltype','price']    

class MachineForm(forms.ModelForm): 
    class Meta: 
        model = Machine
        fields = ['fueltype', 'machine_no', 'company_name','machine_des']


class TankerForm(forms.ModelForm): 
    class Meta: 
        model = Tanker
        fields = ['supplier', 'fueltype', 'tanker_no','tanker_date','quantity','tanker_des']
      


 #Booking form
class FuelBooking(forms.Form):
    choice = ( ('Two Wheel Vehicles','Two Wheel Vehicles'),
               ('Three Wheel Vehicles', 'Three Wheel Vehicles'),
               ('Car – Vehicles','Car – Vehicles'),
             ('Pick Up- Vehicles','Pick Up-Vehicles '),
                ('Bus – Road Vehicles','Bus – Road Vehicles'),
              ('Trucks – Vehicles','Trucks – Vehicles'),
              ('Backhoe – Heavy ','Backhoe – Heavy '),
              ('Tractor –  Vehicles','Tractor – Vehicles'))

    schoice = (('Petrol', 'Petrol'),
               ('Diesel', 'Diesel'),
               ('CNG','CNG'),
               ('LPG','LPG'),
               ('Wash', 'Wash'),
               ('Ethanol', 'Ethanol'),
               ('Bio-Diesel','Bio-Diesel'))
    vehicle_reg_no = forms.CharField(widget=forms.TextInput(),label='Vehicle Registration Number')
    vehicle_name = forms.CharField(widget=forms.TextInput(),label='Vehicle Model')
    vehicle_type = forms.ChoiceField(choices=choice, label='Vehicle Type')
    type_of_fuel = forms.ChoiceField( choices=schoice ,label='Type of fuel')
    fuel_qua = forms.IntegerField(label='Fuel Quantity')

#updatefuelstatus
class DateInput(forms.DateInput):
    input_type = 'date'

class updatefuel(forms.ModelForm):
    class Meta:
        model = FuelService
        fields = ['ss','ser_status','finish_date']
        widgets = {
            'finish_date': DateInput()
        }
############
#     
class AdmincustomerForm(forms.ModelForm):
    class Meta:
        model = admincustomer
        fields = ['customer','supplier','tanker','fueltype','fuelquantity','remarks']



class ProfilepicForm(forms.Form):
    class Meta:
        model = profilepic
        fields = ['avatar']