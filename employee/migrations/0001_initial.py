# Generated by Django 3.0.5 on 2020-04-15 17:53

from django.db import migrations, models
from hashlib import md5


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('emp_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
