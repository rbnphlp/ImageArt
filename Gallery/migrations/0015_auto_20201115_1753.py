# Generated by Django 3.1.2 on 2020-11-15 17:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0014_auto_20201115_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Gallery.category'),
        ),
    ]