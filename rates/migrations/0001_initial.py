# Generated by Django 2.2.7 on 2019-11-24 13:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import pyuploadcare.dj.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('project_pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('description', models.CharField(max_length=250)),
                ('website', models.URLField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prof_pic', pyuploadcare.dj.models.ImageField(blank=True)),
                ('bio', models.CharField(max_length=250)),
                ('contact', phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
