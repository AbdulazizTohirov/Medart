# Generated by Django 4.0.6 on 2022-09-13 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_remove_operationg_attented_main_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors_about',
            name='operations',
            field=models.ManyToManyField(null=True, to='main.operationg_attented'),
        ),
    ]