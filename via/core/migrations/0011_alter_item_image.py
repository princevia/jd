# Generated by Django 4.0.3 on 2022-04-25 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_itemimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
