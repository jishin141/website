# Generated by Django 4.1.1 on 2022-11-30 04:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hairoil', '0002_shipping_cart_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('totalamount', models.CharField(max_length=255)),
                ('status', models.CharField(default='pending', max_length=255)),
                ('date', models.CharField(max_length=255)),
                ('uid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hairoil.register_form')),
            ],
        ),
    ]
