# Generated by Django 2.0.2 on 2018-03-03 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_auto_20180205_2355'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomDayAndTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=1)),
                ('begin', models.TimeField()),
                ('end', models.TimeField()),
                ('room', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='course',
            name='days',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end',
        ),
        migrations.RemoveField(
            model_name='course',
            name='room',
        ),
        migrations.AddField(
            model_name='course',
            name='room_day_and_time',
            field=models.ManyToManyField(to='courses.RoomDayAndTime'),
        ),
    ]