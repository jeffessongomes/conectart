# Generated by Django 2.2.4 on 2020-04-09 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20200409_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Our',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('details', models.TextField(verbose_name='detalhes')),
            ],
        ),
    ]
