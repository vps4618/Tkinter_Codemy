from django.urls import path
from . import views

urlpatterns = [
    # int: nummbers
    # str: strings
    # path: whole urls/
    # slug: hyphen-and_underscores_stuff
    # UUID: universally unique identifier
    
    path('',views.home,name='home'),
    path('<int:year>/<str:month>/',views.home,name='home')
]