# Generated by Django 4.2.4 on 2023-08-08 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products', models.TextField()),
                ('number_of_products', models.DecimalField(decimal_places=2, max_digits=6)),
                ('shipping_cost', models.DecimalField(decimal_places=2, max_digits=6)),
                ('delivery_options', models.CharField(max_length=48)),
                ('payment_options', models.CharField(max_length=48)),
            ],
        ),
    ]
