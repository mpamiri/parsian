from django.urls import path , include
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
    path('manage/summary_of_results/add_summary/',views.addsummary,name='addsummary'),
    path('manage/submit_company/',views.company,name='submit_company'),
    path('manage/occupational_disease/',views.occupational_disease,name='occupational_disease'),
    path('manage/occupational_disease/disease_code',views.disease_code,name='disease_code'),
    path('manage/occupational_disease/open_docs',views.open_docs,name='open_docs'),
    path('manage/occupational_disease/summary_of_examinations',views.summary_of_examinations,name='summary_of_examinations'),
    path('manage/occupational_disease/problem',views.problem,name='problem'),  
    path('manage/occupational_disease/specialist',views.specialist,name='specialist'),
    path('manage/occupational_disease/graph',views.graph,name='graph'),  
    path('manage/occupational_disease/solo_output',views.solo_output,name='solo_output'),  
    path('manage/submit_company/add_company',views.addcompany,name='addcompany')    
]
urlpatterns += staticfiles_urlpatterns()