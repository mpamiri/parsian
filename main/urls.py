from django.urls import path
from . import views
urlpatterns =[
    path('main/start',views.first)
]