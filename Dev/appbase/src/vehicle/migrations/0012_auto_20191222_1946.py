# Generated by Django 2.2.5 on 2019-12-22 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_auto_20191222_1943'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='image',
            new_name='images',
        ),
    ]
