# Generated by Django 4.2.3 on 2023-08-08 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='Category',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='Created_at',
            new_name='created_at',
        ),
    ]
