# Generated by Django 4.1.7 on 2023-08-29 15:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0005_alter_student_data_mob'),
    ]

    operations = [
        migrations.CreateModel(
            name='chats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=20)),
                ('reciver', models.CharField(max_length=20)),
                ('message', models.TextField(max_length=300)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 8, 29, 21, 19, 52, 515039))),
            ],
        ),
    ]
