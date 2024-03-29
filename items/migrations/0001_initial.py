# Generated by Django 3.2.13 on 2022-12-20 02:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ItemId', models.AutoField(primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=100)),
                ('MRP', models.FloatField(default=0)),
            ],
            options={
                'db_table': 'item',
            },
        ),
        migrations.CreateModel(
            name='ItemUnits',
            fields=[
                ('ItemUnitId', models.AutoField(primary_key=True, serialize=False)),
                ('UnitId', models.IntegerField()),
                ('NoOfUnits', models.FloatField()),
                ('Rate', models.FloatField()),
                ('ItemId', models.ForeignKey(db_column='ItemId', on_delete=django.db.models.deletion.CASCADE, to='items.item')),
            ],
            options={
                'db_table': 'itemunits',
            },
        ),
    ]
