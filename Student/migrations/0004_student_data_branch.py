# Generated by Django 4.1.7 on 2023-08-29 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0003_student_data_delete_student_dsata'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_data',
            name='branch',
            field=models.TextField(default='NA', max_length=30),
        ),
    ]
