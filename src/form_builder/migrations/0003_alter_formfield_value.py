# Generated by Django 3.2.7 on 2021-09-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form_builder', '0002_formfield_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formfield',
            name='value',
            field=models.TextField(blank=True, null=True),
        ),
    ]