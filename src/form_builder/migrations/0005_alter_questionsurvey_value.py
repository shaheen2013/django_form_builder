# Generated by Django 3.2.7 on 2021-09-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0004_from_questionsurvey'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionsurvey',
            name='value',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]