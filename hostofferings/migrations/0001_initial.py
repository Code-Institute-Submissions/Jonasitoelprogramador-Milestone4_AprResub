# Generated by Django 3.2 on 2022-02-22 14:08

from django.db import migrations, models
import django.db.models.deletion
import hostofferings.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_category', models.CharField(max_length=100)),
                ('work_details', models.TextField()),
                ('offering_image', models.ImageField(default='default.jpg', upload_to=hostofferings.models.path_time)),
                ('random_identifier', models.CharField(max_length=100)),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.host')),
            ],
        ),
    ]
