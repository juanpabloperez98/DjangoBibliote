# Generated by Django 3.2.4 on 2021-07-06 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_alter_libro_cover_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='cover_page',
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]
