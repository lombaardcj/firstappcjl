# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityTemplate',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastchanged_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, null=True, max_length=200)),
                ('vat', models.CharField(blank=True, null=True, max_length=25)),
                ('contactname', models.CharField(blank=True, null=True, max_length=100)),
                ('contactemail', models.EmailField(blank=True, null=True, max_length=254)),
                ('contactphone', models.CharField(blank=True, null=True, max_length=50)),
                ('street', models.CharField(blank=True, null=True, max_length=200)),
                ('postcode', models.CharField(blank=True, null=True, max_length=10)),
                ('city', models.CharField(blank=True, null=True, max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastchanged_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('comment', models.TextField(blank=True, null=True)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=7, default='0.00')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastchanged_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='timekeeper.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectActivity',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('billable', models.BooleanField(default=False)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=7, default='0.00')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=7, default='0.00')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastchanged_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('name', models.ForeignKey(to='timekeeper.ActivityTemplate')),
                ('project', models.ForeignKey(to='timekeeper.Project')),
            ],
        ),
        migrations.CreateModel(
            name='TimeRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('active', models.BooleanField(default=True)),
                ('description', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('delta', models.DateTimeField(blank=True, null=True)),
                ('approved', models.BooleanField()),
                ('fileupload', models.FileField(blank=True, upload_to='', null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('lastchanged_date', models.DateTimeField(blank=True, null=True)),
                ('approved_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(to='timekeeper.Customer')),
                ('project', models.ForeignKey(to='timekeeper.Project')),
                ('projectactivity', models.ForeignKey(to='timekeeper.ProjectActivity')),
            ],
        ),
    ]
