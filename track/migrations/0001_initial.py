# Generated by Django 3.1.7 on 2021-02-27 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rickshaw',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('license', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
            ],
        ),
    ]
