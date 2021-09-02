from django.db import models


# Create your models here.


# class QuestionSurvey(models.Model):
#     FIELD_CHOICE = [
#         ('text', 'Text'),
#         ('file', 'File'),
#         ('email', 'Email'),
#         ('checkbox', 'Checkbox'),
#         ('color', 'Color'),
#         ('date', 'Date'),
#         ('hidden', 'Hidden'),
#         ('password', 'Password'),
#         ('radio', 'Radio'),
#         ('textarea', 'Textarea'),
#         ('select', 'Select')
#     ]
#     label = models.CharField(max_length=255)
#     field_type = models.CharField(choices=FIELD_CHOICE, max_length=255)
#     required = models.BooleanField(default=False)
#     value = models.JSONField(blank=True, null=True)
#     order = models.IntegerField()

class FormField(models.Model):
    FIELD_CHOICE = [
            ('text', 'Text'),
            ('file', 'File'),
            ('email', 'Email'),
            ('checkbox', 'Checkbox'),
            ('color', 'Color'),
            ('date', 'Date'),
            ('hidden', 'Hidden'),
            ('password', 'Password'),
            ('radio', 'Radio'),
            ('textarea', 'Textarea'),
            ('select', 'Select')
        ]
    title = models.CharField(max_length=255)
    type = models.CharField(choices=FIELD_CHOICE, max_length=255)
    value = models.TextField(blank=True, null=True)