# Generated by Django 4.0.3 on 2022-04-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0019_rename_image_1_item_image_remove_item_default_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_1',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_2',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_3',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
