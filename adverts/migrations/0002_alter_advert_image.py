# Generated by Django 5.1.1 on 2024-09-30 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adverts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advert',
            name='image',
            field=models.ImageField(upload_to='adverts_images/'),
        ),
    ]
