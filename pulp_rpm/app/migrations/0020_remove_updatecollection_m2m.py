# Generated by Django 2.2.14 on 2020-08-06 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rpm', '0019_migrate_updatecollection_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='updatecollection',
            name='update_record',
        ),
    ]
