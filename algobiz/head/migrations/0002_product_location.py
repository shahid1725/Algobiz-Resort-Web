# Generated by Django 4.0.1 on 2022-01-26 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('head', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.CharField(max_length=200, null=True),
        ),
    ]