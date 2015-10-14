# Create your models here.

from django.db import models
from django.utils import timezone

class Customer(models.Model):
    author = models.ForeignKey('auth.User')
    active = models.BooleanField(
            default=True)
    name = models.CharField(max_length=200)
    comment = models.TextField(
            blank=True, null=True)
    company = models.CharField(max_length=200,
            blank=True, null=True)
    vat = models.CharField(max_length=25,
            blank=True, null=True)
    contactname = models.CharField(max_length=100,
            blank=True, null=True)
    contactemail = models.EmailField(
            blank=True, null=True)
    contactphone = models.CharField(max_length=50,
            blank=True, null=True)
    street = models.CharField(max_length=200,
            blank=True, null=True)
    postcode = models.CharField(max_length=10,
            blank=True, null=True)
    city = models.CharField(max_length=50,
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    lastchanged_date = models.DateTimeField(
            blank=True, null=True)
            
    def __str__(self):
            return self.name+' ('+str(self.id)+')'


class Project(models.Model):
    author = models.ForeignKey('auth.User')
    customer = models.ForeignKey(Customer)
    active = models.BooleanField(
            default=True)
    name = models.CharField(max_length=200)
    comment = models.TextField(
            blank=True, null=True)
    budget = models.DecimalField(max_digits=7,decimal_places=2,
            default='0.00')
    created_date = models.DateTimeField(
            default=timezone.now)
    lastchanged_date = models.DateTimeField(
            blank=True, null=True)
            
    def __str__(self):
            return self.name

class ActivityTemplate(models.Model):
    author = models.ForeignKey('auth.User')
    active = models.BooleanField(
            default=True)
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    lastchanged_date = models.DateTimeField(
            blank=True, null=True)
            
    def __str__(self):
            return self.name


class ProjectActivity(models.Model):
    author = models.ForeignKey('auth.User')
    project = models.ForeignKey(Project)
    name = models.ForeignKey(ActivityTemplate)
    active = models.BooleanField(
            default=True)
    comment = models.TextField(
            blank=True, null=True)
    billable = models.BooleanField(
            default=False)
    budget = models.DecimalField(max_digits=7,decimal_places=2,
            default='0.00')
    rate = models.DecimalField(max_digits=7,decimal_places=2,
            default='0.00')
    created_date = models.DateTimeField(
            default=timezone.now)
    lastchanged_date = models.DateTimeField(
            blank=True, null=True)
            
    def __str__(self):
            return str(self.name)+' ('+str(self.project)+')'
 

class TimeRecord(models.Model):
    author = models.ForeignKey('auth.User')
    customer = models.ForeignKey(Customer)
    project = models.ForeignKey(Project)
    projectactivity = models.ForeignKey(ProjectActivity)
    active = models.BooleanField(
            default=True)
    description = models.CharField(max_length=200)
    start_date = models.DateTimeField(
            default=timezone.now)
    end_date = models.DateTimeField(
            default=timezone.now)
    delta = models.DateTimeField(
            blank=True, null=True)
    approved = models.BooleanField()
    fileupload = models.FileField(
            blank=True, null=True)
    created_date = models.DateTimeField(
            default=timezone.now)
    lastchanged_date = models.DateTimeField(
            blank=True, null=True)
    approved_date = models.DateTimeField(
            blank=True, null=True)

    def approve(self):
        self.approved = True
        self.approved_date = timezone.now()
        self.save()

    def updateduration(self):
        self.delta = end_date - start_date
        self.save()

    def __str__(self):
        return self.description

