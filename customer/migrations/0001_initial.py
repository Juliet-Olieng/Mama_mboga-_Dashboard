# Generated by Django 4.2.4 on 2023-08-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=48)),
                ('phone_number', models.IntegerField()),
                ('email_address', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=48)),
            ],
        ),
    ]
