# Generated by Django 4.0.3 on 2022-05-12 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_drug_packdrug_pack'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pack',
            old_name='items',
            new_name='drugs',
        ),
        migrations.RenameField(
            model_name='packdrug',
            old_name='item',
            new_name='drug',
        ),
    ]