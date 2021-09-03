from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from form_builder.models import QuestionSurvey, From


class FormSerializer(ModelSerializer):
    class Meta:
        model = From
        fields = ('id', 'label', 'field_type', 'value', 'order')


class FormSaveSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.JSONField(), min_length=1)

    # def validate(self, data):
    #     print('a', data)
    #     raise serializers.ValidationError('jhjvhjvh')

    def create(self, validated_data):
        form = self._save_from(validated_data)
        form_question = self._question_survey(validated_data, form)
        return validated_data

    def update(self, instance, validated_data):
        return instance

    def _save_from(self, validated_date):
        form = From()
        form.title = validated_date['data'][-1]
        form.save()
        return form

    def _question_survey(self, validated_data, form):
        validated_data['data'].pop()
        data = validated_data['data']
        i = 0
        for item in data:
            print(item['id'], )
            question = QuestionSurvey()
            question.label = item['title']
            question.type = item['type']
            question.order = i
            question.value = item['input_value']
            question.form = form
            abc = question.save()
            i = i + 1
        pass
