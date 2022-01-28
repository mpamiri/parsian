from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    path('',views.home),
    path('contact_us/',views.contact_us),
    path('occupational_medicine/',views.occupational_medicine),
    path('services/',views.services),
    path('register/',views.register),
    path('login/',views.login)
]
urlpatterns += staticfiles_urlpatterns()