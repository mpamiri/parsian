from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns =[
    path('',views.home,name= 'home'),
    path('contact_us/',views.contact_us),
    path('occupational_medicine/',views.occupational_medicine),
    path('services/',views.services),
    path('manage/',views.manage),
    path('logout/',views.logoutuser,name='logout'),
    path('manage/summary_of_results/',views.summary,name='summary_of_results'),
    path('login/',views.login,name='login')
]
urlpatterns += staticfiles_urlpatterns()