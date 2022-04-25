# Generated by Django 3.2.6 on 2022-04-18 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_visitordetails'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('mob', models.CharField(max_length=100)),
                ('mob1', models.IntegerField(max_length=10)),
                ('mob2', models.IntegerField(max_length=10)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('hometown', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=30)),
                ('caste', models.CharField(max_length=30)),
                ('nation', models.CharField(max_length=30)),
                ('aadhar', models.IntegerField(max_length=16)),
                ('pan', models.CharField(max_length=8)),
                ('blood', models.CharField(max_length=10)),
                ('allergy', models.CharField(max_length=30)),
                ('guard', models.CharField(max_length=30)),
                ('gaddress', models.CharField(max_length=100)),
                ('gnumber', models.IntegerField(max_length=10)),
                ('rel', models.CharField(max_length=30)),
                ('sphoto', models.FileField(upload_to='')),
                ('aphoto', models.FileField(upload_to='')),
                ('svaccine', models.FileField(upload_to='')),
            ],
        ),
    ]
