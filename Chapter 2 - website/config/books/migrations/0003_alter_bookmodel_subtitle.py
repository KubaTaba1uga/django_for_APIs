# Generated by Django 4.0.1 on 2022-01-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_alter_bookmodel_subtitle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]