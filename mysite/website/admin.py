from django.contrib import admin
from website.models import Contact , Newsletter

# Register your models here.

class ContactAdmin(admin.ModelAdmin): 
    list_display = ("name","created_date")
    list_filter =("name","created_date")
    search_fields = ("name","created_date")
    


admin.site.register(Contact,ContactAdmin)
admin.site.register(Newsletter)
