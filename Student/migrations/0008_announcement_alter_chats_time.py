# Generated by Django 4.1.7 on 2023-11-08 12:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0007_alter_chats_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('title', models.TextField(max_length=100)),
                ('content', models.TextField(max_length=500)),
                ('time', models.DateTimeField(default=datetime.datetime(2023, 11, 8, 17, 43, 56, 19569))),
            ],
        ),
        migrations.AlterField(
            model_name='chats',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 8, 17, 43, 56, 18569)),
        ),
    ]
