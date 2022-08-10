from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('profile/', views.userAccount, name="profile"),
    path('update_schedule', views.updateSchedule, name='update_schedule'),
    path('updateNotes', views.updateNotes, name="updateNotes"),
    path('saveSchedule', views.saveSchedule, name="saveSchedule"),
    path('update_inventory', views.update_inventory, name="update_inventory"),
    #path('inventory_details', views.inventory_details, name='inventory_details'),
    path('saveInventory', views.saveInventory, name='saveInventory'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    #path('calendar', views.calendar, name='calendar'),
    path('update_hydraulic_hose_schedule', views.update_hydraulic_hose_schedule, name='update_hydraulic_hose_schedule'),
    path('saveHydrHoseDate', views.saveHydrHoseDate, name='saveHydrHoseDate'),
]