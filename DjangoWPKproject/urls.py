
from django.contrib import admin
from django.urls import path
import authentication.views
import employe.views
from materiels.views import MaterielListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', authentication.views.login_page, name='login'),
    path('login', authentication.views.login_page, name='login'),
    path('logout/', authentication.views.logout_user, name='logout'),
    path('materiel/', MaterielListView.as_view(), name='materiel_list'),
    path('home/',  authentication.views.home, name='home'),

    path('employes/',  employe.views.employes, name='employes'),
    #employees crud
    path('employee/<int:employee_id>/delete/', employe.views.delete_employee, name='delete_employee'),
    path('employee/<int:employee_id>/edit/', employe.views.edit_employee, name='edit_employee'),




]
