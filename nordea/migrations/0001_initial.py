# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-27 05:39
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('bank', models.CharField(choices=[('BARCLAYS', 'BARCLAYS'), ('HSBC', 'HSBC'), ('NORDEA', 'NORDEA'), ('NATIONWIDE', 'NATIONWIDE'), ('RBS', 'RBS'), ('LLOYDS', 'LLOYDS'), ('SANTANDER', 'SANTANDER')], default='NATIONWIDE', help_text='Bank', max_length=10, verbose_name='Bank')),
                ('name', models.CharField(blank=True, help_text='Account Name', max_length=40, verbose_name='Account Name')),
                ('sortcode', models.CharField(blank=True, help_text='Sort code', max_length=6, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Sort code')),
                ('account_number', models.CharField(help_text='Bank account number', max_length=9, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Account Number')),
                ('sweep_min_balance', models.FloatField(default=0, help_text='Balance before sweeping', verbose_name='Sweep Balance Limit')),
                ('sweep_account', models.ForeignKey(blank=True, help_text='Account to use to sweep from', null=True, on_delete=django.db.models.deletion.CASCADE, to='nordea.Account', verbose_name='Sweep Account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('name', models.CharField(blank=True, help_text='Full name', max_length=60, verbose_name='Name')),
                ('first_name', models.CharField(help_text='First name', max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(help_text='Full name', max_length=30, verbose_name='Last Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('transaction_type', models.CharField(choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')], help_text='Transaction type', max_length=10, verbose_name='Type')),
                ('amount', models.FloatField(default=0.0, help_text='Transaction Amount', verbose_name='Amount')),
                ('description', models.CharField(blank=True, help_text='Transaction description', max_length=250, verbose_name='Description')),
                ('transdate', models.DateTimeField(auto_now=True, help_text='Transaction date and time', verbose_name='Date and Time')),
                ('transaction_id', models.CharField(blank=True, max_length=100, verbose_name='Xero Account ID')),
                ('account', models.ForeignKey(help_text='Bank Account', on_delete=django.db.models.deletion.CASCADE, to='nordea.Account', verbose_name='Account')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nordea.Contact', verbose_name='Xero Contact')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
