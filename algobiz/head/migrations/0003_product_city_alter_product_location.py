# Generated by Django 4.0.1 on 2022-01-27 15:08

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0002_product_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]
