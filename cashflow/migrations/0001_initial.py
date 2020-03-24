# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 18:49
from __future__ import unicode_literals

import cashflow.utilities
import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('bank', models.CharField(choices=[('BARCLAYS', 'BARCLAYS'), ('HSBC', 'HSBC'), ('NORDEA', 'NORDEA'), ('NATIONWIDE', 'NATIONWIDE'), ('RBS', 'RBS'), ('LLOYDS', 'LLOYDS'), ('SANTANDER', 'SANTANDER')], default='NATIONWIDE', max_length=10, verbose_name='Bank')),
                ('name', models.CharField(max_length=40, verbose_name='Account Name')),
                ('sortcode', models.CharField(blank=True, max_length=6, validators=[django.core.validators.MinLengthValidator(6)], verbose_name='Sort Code')),
                ('account_number', models.CharField(max_length=9, validators=[django.core.validators.MinLengthValidator(8)], verbose_name='Account Number')),
                ('currency', models.CharField(choices=[('EURO', 'EURO'), ('USD', 'USD'), ('GBP', 'GBP')], default='GBP', help_text='Currency', max_length=10, verbose_name='Currency')),
                ('sweep_min_balance', models.FloatField(default=0, verbose_name='Sweep Balance Limit')),
                ('account_id', models.CharField(blank=True, max_length=100, verbose_name='Xero Account ID')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
                ('sweep_account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.Account', verbose_name='Sweep Account')),
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
                ('name', models.CharField(blank=True, max_length=60, verbose_name='Name')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('contact_id', models.CharField(blank=True, max_length=100, verbose_name='Xero Contact ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, db_index=True, editable=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('invoice_type', models.CharField(choices=[('PAYABLE', 'Payable'), ('RECEIVABLE', 'Receivable')], help_text='Invoice type', max_length=15, verbose_name='Type')),
                ('number', models.CharField(blank=True, help_text='Invoice number will be autogenerated.', max_length=25, verbose_name='Invoice Number')),
                ('raised', models.DateField(default=datetime.date.today, help_text='Date invoice was raised', verbose_name='Date Raised')),
                ('due', models.DateField(default=cashflow.utilities.due_date, help_text='Date invoice is due', verbose_name='Date Due')),
                ('expected', models.DateField(blank=True, help_text='Date invoice is expected to be paid', null=True, verbose_name='Date Expected')),
                ('planned', models.DateField(blank=True, help_text='Date invoice is planned to be paid', null=True, verbose_name='Date Planned')),
                ('actual', models.DateField(blank=True, help_text='Date invoice was paid', null=True, verbose_name='Date Paid')),
                ('amount', models.FloatField(default=0.0, help_text='Invoice total amount', verbose_name='Amount')),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('UNPAID', 'Unpaid')], default='UNPAID', help_text='Invoice payment status', max_length=10, verbose_name='Status')),
                ('bank_account', models.ForeignKey(help_text='Bank Account to use for Payable Receivables', on_delete=django.db.models.deletion.CASCADE, to='cashflow.Account', verbose_name='Bank Account')),
                ('contact', models.ForeignKey(help_text='Customer/Supplier contact', on_delete=django.db.models.deletion.CASCADE, to='cashflow.Contact', verbose_name='Contact')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0, verbose_name='Loan Balance')),
                ('status', models.CharField(choices=[('PAID', 'Paid'), ('OUTSTANDING', 'Outstanding')], default='OUTSTANDING', help_text='Status of the loan', max_length=15, verbose_name='Status')),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cashflow.Account')),
            ],
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
                ('currency', models.CharField(choices=[('EURO', 'EURO'), ('USD', 'USD'), ('GBP', 'GBP')], default='GBP', help_text='Currency', max_length=10, verbose_name='Currency')),
                ('description', models.CharField(blank=True, help_text='Transaction description', max_length=250, verbose_name='Description')),
                ('transdate', models.DateTimeField(auto_now=True, help_text='Transaction date and time', verbose_name='Date and Time')),
                ('transaction_id', models.CharField(blank=True, max_length=100, verbose_name='Xero Account ID')),
                ('account', models.ForeignKey(help_text='Bank Account', on_delete=django.db.models.deletion.CASCADE, to='cashflow.Account', verbose_name='Account')),
                ('contact', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cashflow.Contact', verbose_name='Xero Contact')),
                ('customer', models.ForeignKey(default=1, help_text='Customer', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Customer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]