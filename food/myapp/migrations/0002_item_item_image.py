# Generated by Django 4.0.5 on 2022-09-29 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.flaticon.com%2Ffree-icon%2Fplaceholder_1377194&psig=AOvVaw1NLHRaB2VEkUAdgScIg42N&ust=1664507905662000&source=images&cd=vfe&ved=0CAsQjRxqFwoTCLje06SFufoCFQAAAAAdAAAAABAE', max_length=1000),
        ),
    ]
