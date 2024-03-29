# Generated by Django 2.2.4 on 2020-04-09 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_admin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image')),
            ],
        ),
        migrations.CreateModel(
            name='TecDashImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, null=True)),
                ('slug', models.CharField(max_length=100, null=True)),
                ('details', models.TextField()),
                ('image', models.ImageField(upload_to='image/dash')),
            ],
        ),
        migrations.AlterField(
            model_name='events',
            name='image_2',
            field=models.ImageField(blank=True, null=True, upload_to='image_event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='image_3',
            field=models.ImageField(blank=True, null=True, upload_to='image_event'),
        ),
        migrations.AlterField(
            model_name='events',
            name='main_image',
            field=models.ImageField(upload_to='image_event'),
        ),
    ]
