# Generated by Django 3.2.4 on 2021-07-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='cover_page',
            field=models.ImageField(null=True, upload_to=None),
        ),
    ]
