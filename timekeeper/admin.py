# Register your models here.
from django.contrib import admin
from .models import Customer
from .models import Project
from .models import ActivityTemplate
from .models import ProjectActivity
from .models import TimeRecord


class CustomerAdmin(admin.ModelAdmin):
        list_filter = ('active',)
        ordering = ('name',)
        readonly_fields = ('created_date',)
        fieldsets = [
            ('Customer Information', {'fields': ['author', 'name', 'active']}),
            ('Comment', {'fields': ['comment'], 'classes': ['collapse']}),
            ('Company Details', {'fields': ['company', 'vat', 'street', 'postcode', 'city'], 'classes': ['collapse']}),
            ('Contact Details', {'fields': ['contactname', 'contactemail', 'contactphone'], 'classes': ['collapse']}),
            ('Date Information', {'fields': ['created_date', 'lastchanged_date'], 'classes': ['collapse']}),
        ]

class ActivityInline(admin.TabularInline):
    model = ProjectActivity
    extra = 0

class ProjectAdmin(admin.ModelAdmin):
        list_filter = ('active',)
        ordering = ('name',)
        readonly_fields = ('created_date',)
        fieldsets = [
            ('Project Information', {'fields': ['author', 'name', 'active', 'customer', 'budget']}),
            ('Comment', {'fields': ['comment'], 'classes': ['collapse']}),
            ('Date Information', {'fields': ['created_date', 'lastchanged_date'], 'classes': ['collapse']}),
        ]
        inlines = [ActivityInline]


class ProjectActivityAdmin(admin.ModelAdmin):
        list_filter = ('active',)
        ordering = ('name',)
        readonly_fields = ('created_date',)
        fieldsets = [
            ('Activity Information', {'fields': ['author', 'name', 'active', 'project']}),
            ('Comment', {'fields': ['comment'], 'classes': ['collapse']}),
            ('Rate Information', {'fields': ['billable', 'budget', 'rate'], 'classes': ['collapse']}),
            ('Date Information', {'fields': ['created_date', 'lastchanged_date'], 'classes': ['collapse']}),
        ]
    
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ActivityTemplate)
#admin.site.register(Project, ProjectActivityAdmin)
admin.site.register(TimeRecord)
