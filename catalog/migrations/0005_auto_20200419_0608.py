# Generated by Django 3.0.5 on 2020-04-19 04:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200418_0951'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_edit_authors', 'Edit authors'),)},
        ),
    ]
