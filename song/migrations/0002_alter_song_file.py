# Generated by Django 4.1.1 on 2022-09-23 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='file',
            field=models.FileField(upload_to='songs/'),
        ),
    ]
