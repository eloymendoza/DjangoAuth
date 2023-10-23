from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    # Campos que son de solo lectura para el administrador
    readonly_fields = ('created', )

# Register your models here.
admin.site.register(Task, TaskAdmin)