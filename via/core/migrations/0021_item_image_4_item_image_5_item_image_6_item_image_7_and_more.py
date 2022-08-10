# Generated by Django 4.0.3 on 2022-05-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_item_image_1_item_image_2_item_image_3'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image_4',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_5',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_6',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_7',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_8',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='image_9',
            field=models.FileField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('J', 'Jewelry'), ('SW', 'Smart watch'), ('DW', 'Designer watch')], max_length=2),
        ),
    ]