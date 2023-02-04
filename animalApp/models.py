
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class user(models.Model):
    CHOICES1 = (
        ('farm_vertinary_officer', 'farm_vertinary_officer'),
        ('farm_owner', 'farm_owner'),
        ('manager', 'manager'),
    )
    user = models.OneToOneField(
        User, db_column='user_id', primary_key=True, verbose_name="Id", on_delete=models.CASCADE)
    username = models.CharField(
        'user_name', db_column='user_name', unique=True, max_length=25)
    rank = models.CharField(
        'User Rank', db_column='user_rank', max_length=25, choices=CHOICES1)
    password = models.CharField(
        "Password", max_length=128, default="pbkdf2_sha256$320000$cdQi5Zu4PSSmZ4kKIZam3q$m2cYjfR+cfF+pHYwlycWsN++5HKk+7xn1foLFaz2ecQ=", db_column="user_password")

    class Meta:
        db_table = 'user'
        ordering = ('-rank',)

    def __str__(self):
        return f" {self.username}  - {self.rank}"


class farm_owner(models.Model):
    owner_id = models.AutoField(
        'Owner Id', db_column='owner_id', primary_key=True)
    owner_name = models.CharField(
        'Owner Name', db_column='owner_name', max_length=200)
    owner_phone_number = models.CharField(
        'Phone Number', unique=True, max_length=10, db_column='owner_phone_number')
    owner_email = models.EmailField(
        'Owner Email', db_column='owner_email', unique=True)
    owner_user_id = models.ForeignKey(
        user, db_column='owner_user_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'farm_owner'
        ordering = ('owner_name',)

    def __str__(self):
        return f'{self.owner_name} {self.owner_phone_number}'


class manager(models.Model):
    manager_id = models.AutoField(
        'Manager Id', primary_key=True, db_column='manager_id')
    manager_name = models.CharField(
        'Manager Name', db_column='manager_name', max_length=255)
    manager_phone_number = models.CharField(
        'Phone Number', unique=True, db_column='manager_phone_number', max_length=10)
    manager_user_id = models.ForeignKey(
        user, db_column='manager_user_id', on_delete=models.CASCADE, verbose_name='Manger_user Id')

    class Meta:
        db_table = 'manager'
        ordering = ('-manager_id',)

    def __str__(self):
        return f"{self.manager_id}-{self.manager_phone_number}"


class farm_vertinary_officer(models.Model):
    vet_id = models.AutoField('Vet Id', primary_key=True, db_column='vet_id')
    vet_name = models.CharField(
        'Vet Name', max_length=255, db_column='vet_name')
    vet_phone_number = models.CharField(
        'Vet Phonenumber', unique=True, max_length=10, db_column='vet_phone_number')
    vet_email = models.EmailField(
        'Vet Email', db_column='vet_email', unique=True)
    vet_user_id = models.ForeignKey(
        user, db_column='vet_user_id', on_delete=models.CASCADE, verbose_name='Vet_user Id')

    class Meta:
        db_table = 'farm_vertinary_officer'
        ordering = ('-vet_id',)

    def __str__(self):
        return f'{self.vet_id} - {self.vet_name} - {self.vet_phone_number}'


class animal_types(models.Model):
    choice = (
        ('Fres-1', 'Fres-1'),
        ('Gars-2', 'Gars-2'),
        ('Jers-3', 'Jers-3'),

    )
    choice1 = (
        ('lactating', 'lacating'),
        ('non-lactating', 'non-lactating'),

    )
    animal_id = models.AutoField(
        'Animal Id', primary_key=True, db_column='animal_id')
    animal_ref = models.CharField(
        'Animal Ref', db_column='animal_ref', max_length=255, unique=True)
    animal_name = models.CharField(
        'Animal Name', db_column='animal_name', max_length=100)
    animal_type_id = models.CharField(
        'Animal_type Id', max_length=25, db_column='animal_type_id', choices=choice)
    animal_status = models.CharField(
        'Animal Status', max_length=25, default=True, choices=choice1, db_column='animal_status')

    class Meta:
        db_table = 'animal_types'
        ordering = ('-animal_id',)

    def __str__(self):
        return f'{self.animal_name}'


class milk_production(models.Model):
    production_id = models.AutoField(
        'Production Id', db_column='production_id', primary_key=True)
    production_animal_id = models.ForeignKey(animal_types, serialize=False, db_column='production_animal_id',
                                             verbose_name='Production_animal Id', on_delete=models.CASCADE)
    production_morning_quantity = models.FloatField(
        'Morning Quantity(litres)', db_column='production_morning_quantity'
    )
    production_mid_morning_quantity = models.FloatField(
        'Mid-morning Quantity(litres)', default=0.0, db_column='production_mid-morning_quantity'
    )
    production_evening_quantity = models.FloatField(
        'Evening Quantity(litres)', db_column='production_evening_quantity'
    )
    production_date = models.DateTimeField(
        'Production Date', auto_now_add=True, db_column='Production_date')
    production_total_quantity = models.FloatField(
        'Total Production(litres)', blank=True, db_column='production_total_quantity')

    class Meta:
        db_table = 'milk_production'
        ordering = ('-production_id',)

    def save(self, *args, **kwargs):
        self.production_total_quantity = self.production_morning_quantity + \
            self.production_evening_quantity + self.production_mid_morning_quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.production_id}-total_milk- {self.production_total_quantity}'.format(self.production_id,
                                                                                           self.production_total_quantity)


class suppliment (models.Model):
    suppliment_id = models.AutoField(
        'Suppliment Id', db_column='suppliment_id', primary_key=True)
    suppliment_name = models.CharField(
        "supplement Name", blank=True, null=True, db_column="suppliment_name", unique=False, max_length=25)
    suppliment_production_id = models.ForeignKey(
        milk_production, default=1, on_delete=models.CASCADE, verbose_name='Production Id', db_column='suppliment_production_id')
    suppliment_production_before = models.FloatField(
        'Production Before Suppliment', default=0.0, db_column='suppliment_production_before')
    suppliment_production_after = models.FloatField(
        'Production After Suppliment', default=0.0, db_column='suppliment_production_after')
    suppliment_production_added = models.FloatField(
        'Production Added', blank=True, default=0.0, db_column='suppliment_production_added')

    suppliment_animal_id = models.ForeignKey(animal_types, db_column='suppliment_animal_id',
                                             verbose_name='Suppliment_animal Id', on_delete=models.CASCADE)
    suppliment_date = models.DateTimeField(
        'Suppliment Date', db_column='suppliment_date', auto_now_add=True)
    suppliment_desc = models.TextField(
        'Suppliment Desc', db_column='suppliment_desc')

    class Meta:
        db_table = 'suppliment'
        ordering = ('suppliment_animal_id',)

    def save(self, *args, **kwargs):
        self.suppliment_production_added = self.suppliment_production_after - \
            self.suppliment_production_before
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.suppliment_desc}-{self.suppliment_id}'


class vet_visists (models.Model):
    vet_visit_id = models.AutoField(
        'Visit Id', db_column='vet_visit_id', primary_key=True)
    vet_animal_id = models.ForeignKey(animal_types, db_column='vet_animal_id',
                                      verbose_name='Vet_animal Id', on_delete=models.CASCADE)
    vet_visist_date = models.DateTimeField(
        'Visist Date', db_column='vet_visist_date', auto_now_add=True)
    vet_visist_desc = models.TextField(
        'Visist Desc', db_column='vet_visist_desc')

    class Meta:
        db_table = 'vet_visists '
        ordering = ('-vet_visit_id',)

    def __str__(self):
        return f'{self.vet_visit_id} - {self.vet_animal_id}'


class vet_visist_prescription (models.Model):
    prescription_id = models.AutoField(
        'Prescription Id', db_column='prescription_id', primary_key=True)
    prescription_vet_visist_id = models.ForeignKey(vet_visists, db_column='prescription_vet_visist_id',
                                                   verbose_name='Prescription_vet_visistId', on_delete=models.CASCADE)
    prescription_disease_name = models.CharField(
        "Disease Name", max_length=30, db_column="prescription_disease_name", default="")
    prescription_description = models.TextField(
        'Prescription Desc', db_column='prescription_description')

    class Meta:
        db_table = 'vet_visist_prescription'
        ordering = ('-prescription_id',)

    def __str__(self):
        return f'{self.prescription_id}-{self.prescription_description}'


class AI_services(models.Model):
    AI_service_id = models.AutoField(
        'Service Id', db_column='AI_service_id', primary_key=True)
    AI_animal_id = models.ForeignKey(animal_types, verbose_name='AI_animal Id',
                                     db_column='AI_animal_id=', on_delete=models.CASCADE)
    AI_vet_id = models.ForeignKey(farm_vertinary_officer, verbose_name='AI_vet Id', db_column='AI_vet_id',
                                  on_delete=models.CASCADE)
    AI_date = models.DateTimeField(
        'AI Date', auto_now_add=True, db_column='AI_date')
    AI_comments = models.TextField('AI comments', db_column='AI_comments')

    class Meta:
        db_table = 'AI_services'
        ordering = ('-AI_service_id',)

    def __str__(self):
        return f'{self.AI_service_id}'
