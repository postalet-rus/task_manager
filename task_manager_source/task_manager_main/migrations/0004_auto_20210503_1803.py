# Generated by Django 3.2 on 2021-05-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager_main', '0003_auto_20210503_1658'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='filepath',
        ),
        migrations.AddField(
            model_name='file',
            name='file',
            field=models.FileField(null=True, upload_to=None),
        ),
    ]
