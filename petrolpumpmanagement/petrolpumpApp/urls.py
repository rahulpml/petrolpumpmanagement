from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('cust_reg/', views.customer_register, name='cust-reg'),
    path('ser_reg/', views.service_register, name='ser-reg'),
    path('login/', views.login, name='login'),
    path('cust_log/', views.customer_login, name='cust-log'),
    path('ser_log/', views.service_login, name='ser-log'),
    path('logout/',views.log_out,name='logout'),
    path('cust_dash/',views.cust_dash,name='cust-dash'),
    path('cust_profile/',views.cust_profile,name='cust-profile'),
    path('ser_dash/',views.ser_dash,name='ser-dash'),
    path('ser_profile/',views.ser_profile,name='ser-profile'),
    path('create_booking/',views.booking,name='create-booking'),
    path('bookings_view/',views.bookings_view,name='bookings-view'),
    path('service_view',views.service_view,name='service-view'),
    path('deleteservice_view/<int:id>/',views.deleteservice_view,name='deleteservice-view'),
    path('update_status/',views.udpate_status,name='update-status'),

    path('Supplier-view',views.Supplier_view,name='homesupplier'),
    path('add/', views.addSupplier, name='add'),
    path('edit/<int:id>/', views.editSupplier, name='edit'),
    path('delete/<int:id>/', views.deleteSupplier, name='delete'),

    path('Fueltype-view',views.Fueltype_view,name='home1'),
    path('addfueltype/', views.addFueltype, name='add1'),
    path('editfueltype/<int:id>/', views.editFueltype, name='edit1'),
    path('deletefueltype/<int:id>/', views.deleteFueltype, name='delete1'),

    path('Fuel-view',views.Fuel_view,name='home2'),
    path('addfuel/', views.addFuel, name='add2'),
    path('editfuel/<int:id>/', views.editFuel, name='edit2'),
    path('deletefuel/<int:id>/', views.deleteFuel, name='delete2'),

    path('Machine-view',views.Machine_view,name='home3'),
    path('addMachine/', views.addMachine, name='add3'),
    path('editMachine/<int:id>/', views.editMachine, name='edit3'),
    path('deleteMachine/<int:id>/', views.deleteMachine, name='delete3'),


    path('Tanker-view',views.Tanker_view,name='home4'),
    path('addTanker/', views.addTanker, name='add4'),
    path('editTanker/<int:id>/', views.editTanker, name='edit4'),
    path('deleteTanker/<int:id>/', views.deleteTanker, name='delete4'),

    path('create_fuelbooking/',views.fuelbooking,name='create-fuelbooking'),
    path('fuelbookings_view/',views.fuelbookings_view,name='fuelbookings-view'),
    path('fuelservice_view',views.fuelservice_view,name='fuelservice-view'),
    path('deletefuelservice_view/<int:id>/',views.deletefuelservice_view,name='deletefuelservice-view'),
    

    path('fuelavailable_view',views.fuelavailable_view,name='fuelavailable-view'),

    path('totalcustomer_view/',views.totalcustomer_view,name='customersview-view'),
    path('delete_customer_view/<int:id>/',views.delete_customer_view,name='deletecustomersview-view'),

    path('admindashboard_view',views.admin_dashboard_view,name='admindashboard-view'),
    path('customerdashboard_view',views.customer_dashboard_view,name='customerdashboard-view'),

    path('items', views.item_list, name='eStore-items'),
    path('cart', views.cart, name='eStore-cart'),
    path('aboutus', views.aboutus_view, name='aboutus'),
    path('contactus', views.contactus_view, name='contactus'),

    path('admincustomer-view', views.admincustomer_view, name='home5'),
    path('addadmincustomer/', views.addadmincustomerview, name='add5'),
    path('editadmincustomer_view/<int:id>/', views.editadmincustomerview, name='edit5'),
    path('deleteadmincustomer_view/<int:id>/', views.deleteadmincustomerview, name='delete5'),

    path('admincustomer_reg_view', views.admincustomerregister, name='admincustomer_reg'),
    path('updatefuel_view/<int:id>/', views.updatefuel_view, name='updatefuel_view'),
    path('updateservice_view/<int:id>/', views.updateservice_view, name='updateservice_view'), 
   
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


#path('fuelupdate_status/',views.fuelupdate_status,name='fuelupdate-status'),