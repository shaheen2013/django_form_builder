from django.db import models


class From(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class QuestionSurvey(models.Model):
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
    label = models.CharField(max_length=255)
    field_type = models.CharField(choices=FIELD_CHOICE, max_length=255)
    # required = models.BooleanField(default=False)
    value = models.CharField(max_length=255, blank=True, null=True)
    order = models.IntegerField()
    form = models.ForeignKey(From, null=True, related_name='form', on_delete=models.SET_NULL)

    def __str__(self):
        return self.label


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

    def __str__(self):
        return self.title
