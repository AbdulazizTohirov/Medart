# Generated by Django 4.1.1 on 2022-09-08 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_aboutus_blog_blog_consulting_doctors_faq_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Aboutus_blog',
            new_name='Aboutus_block',
        ),
        migrations.RenameModel(
            old_name='AboutusblocModel',
            new_name='AboutusblockModel',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='email_title',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='location_title',
        ),
        migrations.RemoveField(
            model_name='contactmodel',
            name='phone_title',
        ),
    ]
