# Generated by Django 4.1.1 on 2022-09-23 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_alter_song_file'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='song',
            table='Audio_store',
        ),
    ]