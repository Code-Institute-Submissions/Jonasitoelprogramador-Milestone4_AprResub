# Generated by Django 3.2.7 on 2021-09-15 14:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='offering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('first_language', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=20)),
                ('work_category', models.CharField(max_length=20)),
                ('work_details', models.TextField()),
                ('email', models.EmailField(max_length=20)),
                ('phonenumber', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
