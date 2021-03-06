# Generated by Django 3.1.2 on 2020-11-11 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0010_auto_20201111_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery_images/Paintings/'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='style_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery_images/Style_pic/'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='upload_pic',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery_images/Upload_pic/'),
        ),
        migrations.AlterField(
            model_name='painting',
            name='upload_style_combined',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery_images/Upload_style_combined/'),
        ),
    ]
