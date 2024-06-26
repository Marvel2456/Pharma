from django.db import models
from accounts.models import Client
import uuid

# Create your models here.

class Age(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    age_range = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self) -> str:
        return self.age_range
    
class Allergy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class History(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.name
    

class RiskFactor(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=200, blank=True, null=True)
    

    def __str__(self) -> str:
        return self.name



class MedicalRecord(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.OneToOneField(Client, on_delete=models.PROTECT, blank=True, null=True)
    Sex_choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    sex = models.CharField(max_length=20, choices=Sex_choice, default="Male", blank=True, null=True)
    age = models.CharField(max_length=200, blank=True, null=True)
    weight = models.CharField(max_length=200, blank=True, null=True)
    height = models.CharField(max_length=200, blank=True, null=True)
    Blood_Group_Choice = (
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
    )
    blood_group = models.CharField(max_length=10, choices=Blood_Group_Choice, default="O+", blank=True, null=True)
    Genotype_Choice = (
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('AC', 'AC'),
        ('SS', 'SS'),
        ('SC', 'SC'),
    )
    genotype = models.CharField(max_length=10, choices=Genotype_Choice, default="AA", blank=True, null=True)

    def __str__(self):
        return self.owner.email
    

class PatientAllergy(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    allergies = models.TextField(blank=True, null=True)
    others = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "patient allergies"

    def __str__(self):
        return self.owner.email


class MedicalHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    histories = models.TextField(blank=True, null=True)
    others = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "medical histories"

    def __str__(self):
        return self.owner.email

class FamilyHistory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Client, on_delete=models.PROTECT, blank=True, null=True)
    risks = models.TextField(blank=True, null=True)
    others = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = "family histories"

    def __str__(self):
        return self.owner.email
    