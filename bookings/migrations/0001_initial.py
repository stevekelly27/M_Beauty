# Generated by Django 3.2 on 2023-02-16 23:53

import bookings.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0002_auto_20230216_2353'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(validators=[bookings.models.Booking.validate_date])),
                ('time', models.IntegerField(choices=[(0, '10AM'), (1, '11AM'), (2, '12PM'), (3, '1PM'), (4, '2PM'), (5, '3PM'), (6, '4PM'), (7, '5PM'), (8, '6PM'), (9, '7PM')])),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='timeslot', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('date', 'time')},
            },
        ),
    ]
