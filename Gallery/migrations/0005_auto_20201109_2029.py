# Generated by Django 3.1.2 on 2020-11-09 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_painting_upload_style_combined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploaded_picture',
            name='category',
        ),
        migrations.AlterField(
            model_name='painting',
            name='style_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='painting',
            name='upload_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.DeleteModel(
            name='Style_picture',
        ),
        migrations.DeleteModel(
            name='Uploaded_Picture',
        ),
    ]
