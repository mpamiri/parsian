from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    path('',views.home_view,name= 'home'),
    path('contact_us/',views.contact_us_view,name='contact_us'),
    path('occupational_medicine/',views.occupational_medicine_view,name='occupational_medicine'),
    path('services/',views.services_view,name='services'),
    path('manage/',views.manage_view,name='manage'),
    path('logout/',views.logoutuser_view,name='logout'),
    path('manage/input/',views.input_view,name='input'),
    path('manage/input/submit_person/',views.submit_person_view,name='submit_person'),
    path('login/',views.login_view,name='login'),
    path('manage/input/summary_of_results/add_summary/',views.addperson_view,name='addsummary'),
    path('manage/input/submit_company/',views.company_view,name='submit_company'),
    path('manage/output/',views.output_view,name='output'),
    path('manage/output/disease_code',views.disease_code_view,name='disease_code'),
    path('manage/output/disease_code/add',views.adddisease_view,name='adddisease'),
    path('manage/output/open_docs',views.open_docs_view,name='open_docs'),
    path('manage/output/summary_of_examinations',views.summary_of_examinations_view,name='summary_of_examinations'),
    path('manage/output/problem',views.problem_view,name='problem'),  
    path('manage/output/specialist',views.specialist_view,name='specialist'),
    path('manage/output/graph',views.graph_view,name='graph'),  
    path('manage/output/solo_output',views.solo_output_view,name='solo_output'),  
    path('manage/submit_company/add_company',views.addcompany_view,name='addcompany')    
]
urlpatterns += staticfiles_urlpatterns()