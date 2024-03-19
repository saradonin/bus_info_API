"""
URL configuration for bus_info_API project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bus_lines.views import CarrierListView, CarrierDetailsView, OrganizerListView, OrganizerDetailsView, LineListView, LineListByOrganizerView, LineListByCarrierView, LineDetailsView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('organizers/', OrganizerListView.as_view(), name="organizer-list"),
    path('organizer/<int:pk>/', OrganizerDetailsView.as_view(),
         name='organizer-details'),
    path('carriers/', CarrierListView.as_view(), name="carrier-list"),
    path('carrier/<int:pk>/', CarrierDetailsView.as_view(), name='carrier-details'),
    path('lines/', LineListView.as_view(), name="line-list"),
    path('lines/by-organizer/<int:organizer_id>/',
         LineListByOrganizerView.as_view(), name='line-list-by-organizer'),
    path('lines/by-carrier/<int:carrier_id>/',
         LineListByCarrierView.as_view(), name='line-list-by-carrier'),
    path('line/<int:pk>/', LineDetailsView.as_view(), name='line-details'),
]
