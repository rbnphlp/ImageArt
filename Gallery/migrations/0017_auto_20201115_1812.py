# Generated by Django 3.1.2 on 2020-11-15 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0016_auto_20201115_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='style_pic',
            field=models.ImageField(default='Style_pic/default_style.jpg', null=True, upload_to='Gallery_images/Style_pic/'),
        ),
    ]