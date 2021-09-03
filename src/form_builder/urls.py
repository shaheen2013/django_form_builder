from django.urls import path
from form_builder.api.form_builder import FormField, FormBuilder

urlpatterns = [
    path('', FormBuilder.as_view(), name="form_builder"),
    path('form_fields/', FormField.as_view(), name="formfield"),

]
