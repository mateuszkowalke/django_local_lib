# Generated by Django 3.0.5 on 2020-04-19 04:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20200419_0608'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit_books', 'Edit books'),)},
        ),
    ]
