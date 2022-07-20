# Generated by Django 4.0.6 on 2022-07-19 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('langage1', models.ImageField(null=True, upload_to='')),
                ('langage2', models.ImageField(null=True, upload_to='')),
                ('langage3', models.ImageField(null=True, upload_to='')),
                ('langage4', models.ImageField(null=True, upload_to='')),
                ('repository', models.CharField(max_length=200)),
            ],
        ),
    ]