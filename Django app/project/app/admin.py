from django.contrib import admin
from app.models import Project, Tasks

# Register your models here.

# configure admin panel
class ProjectAdmin(admin.ModelAdmin):
    list_filter = ['name','start_date','end_date']
    
# register our apps
admin.site.register(Project, ProjectAdmin)
admin.site.register(Tasks)
