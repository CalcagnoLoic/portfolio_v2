# Generated by Django 4.0.6 on 2022-07-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addprojects',
            name='langage3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='addprojects',
            name='langage4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
