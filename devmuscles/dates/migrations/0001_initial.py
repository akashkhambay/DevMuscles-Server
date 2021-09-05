# Generated by Django 3.2.7 on 2021-09-03 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='date',
            fields=[
                ('id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('workout_id', models.CharField(max_length=300)),
                ('user_id', models.CharField(max_length=500)),
                ('date', models.CharField(max_length=10)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]
