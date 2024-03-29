# Generated by Django 4.0.6 on 2022-08-09 14:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_bearingsreplace_brushcomponent_bearingsduedate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='HydraulicHoses',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('brushID', models.IntegerField()),
                ('dateReplaced', models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy')),
                ('dueDate', models.DateField(default=datetime.date(2022, 11, 9), verbose_name='%mm/%dd/%yyyy')),
                ('siteCode', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='bearings',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='bearingsDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='cloth',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='clothDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='motor',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='motorDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='shaft',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='shaftDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='shocks',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='shocksDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='upperBearings',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='brushcomponent',
            name='upperBearingsDueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='dateReplaced',
            field=models.DateField(default=datetime.date(2022, 8, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
        migrations.AlterField(
            model_name='maintenance',
            name='dueDate',
            field=models.DateField(default=datetime.date(2023, 2, 9), verbose_name='%mm/%dd/%yyyy'),
        ),
    ]
