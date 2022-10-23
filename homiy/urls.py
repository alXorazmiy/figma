from django.urls import path 
from .views import HomePageView, DonePageView, DashboardPageView,HomiylarPageView,TalabalarPageView,HomiylarSinglePageView, \
                    TalabalarAddPageView,TalabalarSinglePageView

urlpatterns = [
    path('', HomePageView, name = 'home'),
    path('done/', DonePageView, name = 'done.html'),
    path('dashboard/', DashboardPageView, name = 'admin_dashboard'),
    path('homiylar/', HomiylarPageView, name = 'admin_homiylar'),
    path('homiylar/<int:pk>', HomiylarSinglePageView, name = 'admin_homiylar_single'),
    path('talabalar/', TalabalarPageView, name = 'admin_talabalar'),
    path('talabalar/add/', TalabalarAddPageView, name = 'admin_talabalar_add'),
    path('talabalar/<int:pk>/', TalabalarSinglePageView, name = 'admin_talabalar_single'),
]
