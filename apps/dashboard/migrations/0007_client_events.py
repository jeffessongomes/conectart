# Generated by Django 2.2.4 on 2020-04-14 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200414_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='events',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.Events'),
        ),
    ]
