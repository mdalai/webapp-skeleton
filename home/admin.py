from django.contrib import admin
from .models import Applications, Userapps

# Register your models here.

class ApplicationsAdmin(admin.ModelAdmin):
  fields = ['name','description','color','defaultstatus', 'link']
  list_display =('name','description','color','defaultstatus', 'link')
  list_filter=['defaultstatus']
  search_fields=['description']

admin.site.register(Applications,ApplicationsAdmin)
