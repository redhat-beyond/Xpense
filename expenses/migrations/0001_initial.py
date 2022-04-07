# Generated by Django 4.0.3 on 2022-04-06 21:11

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house', '0002_add_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='', max_length=250)),
                ('category', models.CharField(choices=[('Rent', 'Rent'), ('Mortgage', 'Mortgage'), ('Bills', 'Bills'), ('Transportation', 'Transportation'), ('Clothing', 'Clothing'), ('Healthcare', 'Healthcare'), ('Food', 'Food'), ('Insurance', 'Insurance'), ('Kids', 'Kids'), ('Culture', 'Culture'), ('Vacations', 'Vacations'), ('Other', 'Other')], default='Other', max_length=32)),
                ('amount', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(verbose_name=datetime.datetime(2022, 4, 6, 21, 11, 38, 920130, tzinfo=utc))),
                ('house_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
            ],
        ),
    ]
