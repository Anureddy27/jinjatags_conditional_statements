from django.urls import path
from app1.views import *
app1_name='anu'
urlpatterns = [
    path('conditions/',conditions,name='conditions'),
]
