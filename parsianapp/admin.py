from django.contrib import admin
from .models import summary_of_results,submit_company,disease

admin.site.register(summary_of_results)
admin.site.register(submit_company)
admin.site.register(disease)
