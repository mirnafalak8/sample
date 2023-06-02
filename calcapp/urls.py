from .import views
from django.urls import path

urlpatterns =[
    path('',views.loadcalculator,name='loadcalculator'),
    path('calc',views.calc,name='calc')
]