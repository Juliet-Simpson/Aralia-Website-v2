# Generated by Django 4.0.5 on 2022-09-04 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investorupdate',
            name='created_on',
            field=models.DateTimeField(),
        ),
    ]
