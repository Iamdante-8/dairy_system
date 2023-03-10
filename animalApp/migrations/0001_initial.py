# Generated by Django 4.0.5 on 2022-07-15 19:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='animal_types',
            fields=[
                ('animal_id', models.AutoField(db_column='animal_id', primary_key=True, serialize=False, verbose_name='Animal Id')),
                ('animal_ref', models.CharField(db_column='animal_ref', max_length=255, unique=True, verbose_name='Animal Ref')),
                ('animal_name', models.CharField(db_column='animal_name', max_length=100, verbose_name='Animal Name')),
                ('animal_type_id', models.CharField(choices=[('Fres-1', 'Fres-1'), ('Gars-2', 'Gars-2'), ('Jers-3', 'Jers-3')], db_column='animal_type_id', max_length=25, verbose_name='Animal_type Id')),
                ('animal_status', models.CharField(choices=[('lactating', 'lacating'), ('non-lactating', 'non-lactating')], db_column='animal_status', default=True, max_length=25, verbose_name='Animal Status')),
            ],
            options={
                'db_table': 'animal_types',
                'ordering': ('-animal_id',),
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('user', models.OneToOneField(db_column='user_id', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='Id')),
                ('username', models.CharField(db_column='user_name', max_length=25, unique=True, verbose_name='user_name')),
                ('rank', models.CharField(choices=[('farm_vertinary_officer', 'farm_vertinary_officer'), ('farm_owner', 'farm_owner'), ('manager', 'manager')], db_column='user_rank', max_length=25, verbose_name='User Rank')),
                ('password', models.CharField(db_column='user_password', default='pbkdf2_sha256$320000$cdQi5Zu4PSSmZ4kKIZam3q$m2cYjfR+cfF+pHYwlycWsN++5HKk+7xn1foLFaz2ecQ=', max_length=128, verbose_name='Password')),
            ],
            options={
                'db_table': 'user',
                'ordering': ('-rank',),
            },
        ),
        migrations.CreateModel(
            name='vet_visists',
            fields=[
                ('vet_visit_id', models.AutoField(db_column='vet_visit_id', primary_key=True, serialize=False, verbose_name='Visit Id')),
                ('vet_visist_date', models.DateTimeField(auto_now_add=True, db_column='vet_visist_date', verbose_name='Visist Date')),
                ('vet_visist_desc', models.TextField(db_column='vet_visist_desc', verbose_name='Visist Desc')),
                ('vet_animal_id', models.ForeignKey(db_column='vet_animal_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.animal_types', verbose_name='Vet_animal Id')),
            ],
            options={
                'db_table': 'vet_visists ',
                'ordering': ('-vet_visit_id',),
            },
        ),
        migrations.CreateModel(
            name='vet_visist_prescription',
            fields=[
                ('prescription_id', models.AutoField(db_column='prescription_id', primary_key=True, serialize=False, verbose_name='Prescription Id')),
                ('prescription_description', models.TextField(db_column='prescription_description', verbose_name='Prescription Desc')),
                ('prescription_vet_visist_id', models.ForeignKey(db_column='prescription_vet_visist_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.vet_visists', verbose_name='Prescription_vet_visistId')),
            ],
            options={
                'db_table': 'vet_visist_prescription',
                'ordering': ('-prescription_id',),
            },
        ),
        migrations.CreateModel(
            name='suppliment',
            fields=[
                ('suppliment_id', models.AutoField(db_column='suppliment_id', primary_key=True, serialize=False, verbose_name='Suppliment Id')),
                ('suppliment_date', models.DateTimeField(auto_now_add=True, db_column='suppliment_date', verbose_name='Suppliment Date')),
                ('suppliment_desc', models.TextField(db_column='suppliment_desc', verbose_name='Suppliment Desc')),
                ('suppliment_animal_id', models.ForeignKey(db_column='suppliment_animal_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.animal_types', verbose_name='Suppliment_animal Id')),
            ],
            options={
                'db_table': 'suppliment',
                'ordering': ('-suppliment_id',),
            },
        ),
        migrations.CreateModel(
            name='milk_production',
            fields=[
                ('production_id', models.AutoField(db_column='production_id', primary_key=True, serialize=False, verbose_name='Production Id')),
                ('production_morning_quantity', models.FloatField(db_column='production_morning_quantity', verbose_name='Morning Quantity(litres)')),
                ('production_mid_morning_quantity', models.FloatField(db_column='production_mid-morning_quantity', default=0.0, verbose_name='Mid-morning Quantity(litres)')),
                ('production_evening_quantity', models.FloatField(db_column='production_evening_quantity', verbose_name='Evening Quantity(litres)')),
                ('production_date', models.DateTimeField(auto_now_add=True, db_column='Production_date', verbose_name='Production Date')),
                ('production_total_quantity', models.FloatField(blank=True, db_column='production_total_quantity', verbose_name='Total Production(litres)')),
                ('production_animal_id', models.ForeignKey(db_column='production_animal_id', on_delete=django.db.models.deletion.CASCADE, serialize=False, to='animalApp.animal_types', verbose_name='Production_animal Id')),
            ],
            options={
                'db_table': 'milk_production',
                'ordering': ('-production_date',),
            },
        ),
        migrations.CreateModel(
            name='manager',
            fields=[
                ('manager_id', models.AutoField(db_column='manager_id', primary_key=True, serialize=False, verbose_name='Manager Id')),
                ('manager_name', models.CharField(db_column='manager_name', max_length=255, verbose_name='Manager Name')),
                ('manager_phone_number', models.CharField(db_column='manager_phone_number', max_length=10, unique=True, verbose_name='Phone Number')),
                ('manager_user_id', models.ForeignKey(db_column='manager_user_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.user', verbose_name='Manger_user Id')),
            ],
            options={
                'db_table': 'manager',
                'ordering': ('-manager_id',),
            },
        ),
        migrations.CreateModel(
            name='farm_vertinary_officer',
            fields=[
                ('vet_id', models.AutoField(db_column='vet_id', primary_key=True, serialize=False, verbose_name='Vet Id')),
                ('vet_name', models.CharField(db_column='vet_name', max_length=255, verbose_name='Vet Name')),
                ('vet_phone_number', models.CharField(db_column='vet_phone_number', max_length=10, unique=True, verbose_name='Vet Phonenumber')),
                ('vet_email', models.EmailField(db_column='vet_email', max_length=254, unique=True, verbose_name='Vet Email')),
                ('vet_user_id', models.ForeignKey(db_column='vet_user_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.user', verbose_name='Vet_user Id')),
            ],
            options={
                'db_table': 'farm_vertinary_officer',
                'ordering': ('-vet_id',),
            },
        ),
        migrations.CreateModel(
            name='farm_owner',
            fields=[
                ('owner_id', models.AutoField(db_column='owner_id', primary_key=True, serialize=False, verbose_name='Owner Id')),
                ('owner_name', models.CharField(db_column='owner_name', max_length=200, verbose_name='Owner Name')),
                ('owner_phone_number', models.CharField(db_column='owner_phone_number', max_length=10, unique=True, verbose_name='Phone Number')),
                ('owner_email', models.EmailField(db_column='owner_email', max_length=254, unique=True, verbose_name='Owner Email')),
                ('owner_user_id', models.ForeignKey(db_column='owner_user_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.user')),
            ],
            options={
                'db_table': 'farm_owner',
                'ordering': ('owner_name',),
            },
        ),
        migrations.CreateModel(
            name='AI_services',
            fields=[
                ('AI_service_id', models.AutoField(db_column='AI_service_id', primary_key=True, serialize=False, verbose_name='Service Id')),
                ('AI_date', models.DateTimeField(auto_now_add=True, db_column='AI_date', verbose_name='AI Date')),
                ('AI_comments', models.TextField(db_column='AI_comments', verbose_name='AI comments')),
                ('AI_animal_id', models.ForeignKey(db_column='AI_animal_id=', on_delete=django.db.models.deletion.CASCADE, to='animalApp.animal_types', verbose_name='AI_animal Id')),
                ('AI_vet_id', models.ForeignKey(db_column='AI_vet_id', on_delete=django.db.models.deletion.CASCADE, to='animalApp.farm_vertinary_officer', verbose_name='AI_vet Id')),
            ],
            options={
                'db_table': 'AI_services',
                'ordering': ('-AI_service_id',),
            },
        ),
    ]
