from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    path('',views.home,name= 'home'),
    path('contact_us/',views.contact_us),
    path('occupational_medicine/',views.occupational_medicine),
    path('services/',views.services),
    path('manage/',views.manage),
    path('logout/',views.logout,name='logout'),
    path('login/',views.login,name='login')
]
urlpatterns += staticfiles_urlpatterns()