# Generated by Django 2.2.4 on 2020-04-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='whatsapp',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
