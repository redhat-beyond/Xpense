import uuid
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30)

    def create_country(name):
        country = Country(name=name)
        country.save()
        return country

    def __str__(self):
        return self.name


class City(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def create_city(name, country):
        city = City(name=name, country=country)
        city.save()
        return city

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
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    public = models.BooleanField(default=False)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    parent_profession_1 = models.CharField(max_length=50, choices=Job.choices, default=Job.OTHER)
    parent_profession_2 = models.CharField(max_length=50, choices=Job.choices, default=Job.OTHER)
    income = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    children = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0)])
    description = models.TextField(max_length=250, default='')

    @staticmethod
    def create_house(user, public, country, city, parent_profession_1, parent_profession_2, income, children):
        house = House(
            user=user,
            public=public,
            country=country,
            city=city,
            parent_profession_1=parent_profession_1,
            parent_profession_2=parent_profession_2,
            income=income,
            children=children,
        )
        house.save()
        return house

    def __str__(self):
        return self.user.username
