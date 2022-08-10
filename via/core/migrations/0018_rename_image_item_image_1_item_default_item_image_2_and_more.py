# Generated by Django 4.0.3 on 2022-04-25 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_alter_item_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='image',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='item',
            name='default',
            field=models.BooleanField(default=False),
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
        migrations.DeleteModel(
            name='ItemImage',
        ),
    ]
