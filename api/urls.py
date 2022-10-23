from django.urls import path 
from .views import HomiylarPage, HomiylarDetailPage, HomePage, TalabalarAPIView, TalabalarDetailAPIView, TalabalarAddAPIView


urlpatterns = [
    path('', HomePage.as_view()),
    path('homiylar/', HomiylarPage.as_view()),
    path('homiylar/<int:pk>', HomiylarDetailPage.as_view()),
    path('talabalar/', TalabalarAPIView.as_view()),
    path('talabalar/<int:pk>', TalabalarDetailAPIView.as_view()),
    path('talabalar/add',TalabalarAddAPIView.as_view()),
]