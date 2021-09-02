from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from form_builder.models import FormField


class FormFieldSerializer(ModelSerializer):
    class Meta:
        model = FormField
        fields = ('id', 'title', 'type', 'value')

