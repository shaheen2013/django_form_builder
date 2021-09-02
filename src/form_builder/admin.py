from django.contrib import admin

# Register your models here.
from form_builder.models import FormField


@admin.register(FormField)
class FormFieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'type')