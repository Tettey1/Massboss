# Generated by Django 4.1.4 on 2023-05-16 22:07

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='image',
            field=models.ImageField(upload_to='song_images', validators=[django.core.validators.FileExtensionValidator(['jpg', 'png'])]),
        ),
    ]
