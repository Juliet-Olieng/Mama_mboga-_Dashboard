# Generated by Django 4.2.4 on 2023-08-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=6)),
                ('payment_method', models.CharField(max_length=32)),
                ('date', models.DateField()),
                ('receipt', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=32)),
                ('order', models.CharField(max_length=32)),
            ],
        ),
    ]
