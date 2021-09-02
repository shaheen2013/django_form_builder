from django.urls import path
from form_builder.api.form_builder import FormField

urlpatterns = [
    path('form_fields/', FormField.as_view(), name="formfield"),
]
