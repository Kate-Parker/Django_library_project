from django.urls import path
from . import views

urlpatterns = [
    path('livre/',views.api_livres,name='api_livre'), #returns views from api_folder
]