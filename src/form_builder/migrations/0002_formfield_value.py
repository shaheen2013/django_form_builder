# Generated by Django 3.2.7 on 2021-09-02 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='formfield',
            name='value',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
