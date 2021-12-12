# Generated by Django 3.2.10 on 2021-12-12 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cycle',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('seed', models.BooleanField(default=False)),
                ('clone', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('name', models.CharField(max_length=60)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growop.plant')),
            ],
        ),
        migrations.CreateModel(
            name='Tent',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('lightWatts', models.IntegerField(blank=True, default=None)),
                ('numOfLights', models.IntegerField(default=1)),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growop.cycle')),
            ],
        ),
        migrations.CreateModel(
            name='Sensor_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('temp', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='')),
                ('humidity', models.DecimalField(decimal_places=2, max_digits=5, null=True, verbose_name='')),
                ('sensor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growop.sensor')),
            ],
        ),
        migrations.AddField(
            model_name='sensor',
            name='tent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growop.tent'),
        ),
        migrations.AddField(
            model_name='plant',
            name='tent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='growop.tent'),
        ),
    ]
