# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 18:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cashflow', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Consent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('account', models.ForeignKey(help_text='Bank Account', on_delete=django.db.models.deletion.CASCADE, to='cashflow.Account', verbose_name='Account')),
                ('customer', models.ForeignKey(default=1, help_text='Customer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'ordering': ('account',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('title', models.CharField(max_length=30)),
                ('accounts', models.ManyToManyField(to='cashflow.Account')),
                ('customer', models.ForeignKey(default=1, help_text='Customer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]