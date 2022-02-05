from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    path('',views.home,name= 'home'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('occupational_medicine/',views.occupational_medicine,name='occupational_medicine'),
    path('services/',views.services,name='services'),
    path('manage/',views.manage,name='manage'),
    path('logout/',views.logoutuser,name='logout'),
    path('manage/summary_of_results/',views.summary,name='summary_of_results'),
    path('login/',views.login,name='login'),
    path('manage/summary_of_results/add/',views.addsummary,name='add')
]
urlpatterns += staticfiles_urlpatterns()