# Generated by Django 3.2.6 on 2022-03-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email_id', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
    ]
