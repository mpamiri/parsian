from django.urls import path , include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns =[
    path('',views.home_view,name= 'home'),
    path('contact_us/',views.contact_us_view,name='contact_us'),
    path('occupational_medicine/',views.occupational_medicine_view,name='occupational_medicine'),
    path('services/',views.services_view,name='services'),
    path('logout/',views.logoutuser_view,name='logout'),
    path('input/',views.input_view,name='input'),
    path('input/submit_person/',views.submit_person_view,name='submit_person'),
    path('login/',views.login_view,name='login'),
    path('input/summary_of_results/add_summary/',views.addperson_view,name='addsummary'),
    path('input/submit_course/',views.submit_course_view,name='submit_course'),
    path('input/submit_company/',views.submit_company_view,name='submit_company'),
    path('output/',views.output_view,name='output'),
    path('output/disease_code',views.disease_code_view,name='disease_code'),
    path('output/disease_code/pdf',views.disease_pdf_view,name='disease_pdf'),
    path('output/add',views.adddisease_view,name='adddisease'),
    path('input/examinations/add',views.addexaminations_view,name='addexaminations'),
    path('output/open_docs',views.open_docs_view,name='open_docs'),
    path('output/open_docs/pdf',views.open_docs_pdf_view,name='open_pdf'),
    path('output/summary_of_examinations',views.summary_of_examinations_view,name='summary_of_examinations'),
    path('output/summary_of_examinations/pdf',views.summary_of_examinations_pdf_view,name='summary_pdf'),
    path('output/problem',views.problem_view,name='problem'),  \
    path('output/problem/pdf',views.problem_pdf_view,name='problem_pdf'), 
    path('output/examinations_output',views.examinations_output_view,name='examinations_output'),  
    path('output/examinations_output/add',views.addexaminations_output_view,name='addexaminationsoutput'),
    path('output/examinations_output/pdf',views.examinations_output_pdf_view,name='examinations_pdf'),
    path('output/specialist',views.specialist_view,name='specialist'),
    path('output/graph',views.graph_view,name='graph'),  
    path('output/graph/pdf',views.graph_pdf_view,name='graph_pdf'),  
    path('output/solo_output',views.solo_output_view,name='solo_output'),  
    path('output/solo_output/pdf',views.solo_pdf_view,name='solo_pdf'),
    path('submit_company/add_company',views.addcompany_view,name='addcompany'),
    path('submit_course/add_course',views.addcourse_view,name='addcourse'),
    path('input/examinations',views.examinations_view,name='examinations'),
    path('output/solo_output/add_order',views.addorder_view,name='addorder')    
]
urlpatterns += staticfiles_urlpatterns()