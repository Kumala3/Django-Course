# Generated by Django 5.0.6 on 2024-06-11 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer360', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('channel', models.CharField(choices=[('phone', 'Phone'), ('sms', 'SMS'), ('email', 'Email'), ('letter', 'Letter')], max_length=15)),
                ('direction', models.CharField(choices=[('inbound', 'Inbound'), ('outbound', 'Outbound')], max_length=10)),
                ('interaction_date', models.DateField(auto_now_add=True)),
                ('summary', models.TextField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer360.customer')),
            ],
        ),
    ]