from django.db import models
from django.core.validators import MinValueValidator


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Job(models.TextChoices):
    TEACHER = 'Teacher'
    STUDENT = 'Student'
    PROGRAMMER = 'Programmer'
    ARTIST = 'Artist'
    MANAGER = 'Manager'
    ARMY = 'Army'
    POLICE = 'Police'
    DOCTOR = 'Doctor'
    VET = 'Vet'
    NURSE = 'Nurse'
    TECHNICHIAN = 'Technichian'
    CLEANER = 'Cleaner'
    OTHER = 'Other'
    UNEMPLOYED = 'Unemployed'


class House(models.Model):
    house_id = models.IntegerField(primary_key=True, validators=[
                                   MinValueValidator(0)], default=0)
    name = models.CharField(max_length=50)
    public = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    parent_profession_1 = models.CharField(max_length=50, choices=Job.choices,
                                           default=Job.OTHER)
    parent_profession_2 = models.CharField(max_length=50, choices=Job.choices,
                                           default=Job.OTHER)
    income = models.IntegerField(null=True, blank=True)
    children = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
