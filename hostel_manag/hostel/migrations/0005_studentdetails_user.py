# Generated by Django 3.2.6 on 2022-04-30 13:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hostel', '0004_studentdetails_certi_alter_studentdetails_aadhar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]