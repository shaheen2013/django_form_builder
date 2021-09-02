from django.http import JsonResponse
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin

from form_builder.models import FormField
from form_builder.serializers.form_field_serializer import FormFieldSerializer


class GenericOrderView(GenericAPIView):
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer

    class Meta:
        abstract = True


class FormField(CreateModelMixin, ListModelMixin, GenericOrderView):

    def get(self, request, *args, **kwargs):
        form_fields = self.queryset.filter()
        serialize = FormFieldSerializer(form_fields, many=True)
        return JsonResponse(list(serialize.data), safe=False)
