# Generated by Django 2.2.2 on 2019-12-13 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MobileImages',
            fields=[
                ('mobile_image_id', models.AutoField(db_column='id_mobile_image', primary_key=True, serialize=False)),
                ('latitude', models.FloatField(db_column='latitude', unique=True)),
                ('longitude', models.FloatField(db_column='longitude')),
                ('apparent_height', models.FloatField(db_column='apparent_height')),
                ('estimated_height', models.FloatField(db_column='estimated_height')),
                ('diameter', models.FloatField(db_column='diameter')),
                ('biomass', models.FloatField(db_column='biomass')),
                ('carbon_content', models.FloatField(db_column='carbon_content')),
                ('estimated_distance', models.FloatField(db_column='estimated_distance')),
                ('actual_distance', models.FloatField(db_column='actual_distance')),
                ('date_time', models.DateTimeField(db_column='date_time')),
            ],
            options={
                'db_table': 'mobile_images',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(db_column='id_user', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, db_column='name', max_length=100, null=True)),
                ('field_of_interest', models.CharField(blank=True, db_column='field_of_interest', max_length=200, null=True)),
                ('organization', models.CharField(blank=True, db_column='organization', max_length=250, null=True)),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserMobile',
            fields=[
                ('user_mobile_id', models.AutoField(db_column='id_user_mobile', primary_key=True, serialize=False)),
                ('imei_number', models.IntegerField(db_column='imei_number', unique=True)),
                ('object_known_distance', models.FloatField(blank=True, db_column='object_known_distance', null=True)),
                ('object_known_width', models.FloatField(blank=True, db_column='object_known_width', null=True)),
                ('object_apparent_width', models.FloatField(blank=True, db_column='object_apparent_width', null=True)),
                ('screen_width', models.FloatField(blank=True, db_column='screen_width', null=True)),
                ('screen_height', models.FloatField(blank=True, db_column='screen_height', null=True)),
                ('mobile_focal_length', models.FloatField(db_column='mobile_focal_length')),
            ],
            options={
                'db_table': 'users_mobile',
                'managed': False,
            },
        ),
    ]
