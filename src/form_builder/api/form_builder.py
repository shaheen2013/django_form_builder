from django.http import JsonResponse
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response

from form_builder.models import FormField, From
from form_builder.serializers.form_field_serializer import FormFieldSerializer
from form_builder.serializers.form_builder_serializer import FormSerializer, FormSaveSerializer


class GenericFromFieldView(GenericAPIView):
    queryset = FormField.objects.all()
    serializer_class = FormFieldSerializer

    class Meta:
        abstract = True


class GenericFromView(GenericAPIView):
    queryset = From.objects.all()
    serializer_class = FormSerializer

    class Meta:
        abstract = True


class FormField(CreateModelMixin, ListModelMixin, GenericFromFieldView):

    def get(self, request, *args, **kwargs):
        form_fields = self.queryset.filter()
        serialize = FormFieldSerializer(form_fields, many=True)
        return JsonResponse(list(serialize.data), safe=False)


class FormBuilder(CreateModelMixin, GenericAPIView):
    serializer_class = FormSaveSerializer

    # def get(self, request, *args, **kwargs):
    #     form_fields = self.queryset.filter()
    #     serialize = FormSerializer(form_fields, many=True)
    #     return JsonResponse(list(serialize.data), safe=False)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return Response({'message': 'Form generated successfully'})


