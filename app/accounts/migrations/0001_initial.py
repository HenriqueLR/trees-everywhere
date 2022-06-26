# Generated by Django 3.2.13 on 2022-06-26 00:39

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, validators=[django.core.validators.RegexValidator(re.compile('[a-zA-Z]'), 'The username can only contain letters, digits or the following characters: @/./+/-/_', 'invalid')], verbose_name='Username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_active', models.BooleanField(default=False, verbose_name='Active Status')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Staff Status')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Updated At')),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'User',
                'db_table': 'user',
                'ordering': ['-date_joined'],
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created At')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Description')),
                ('cpf', models.CharField(db_column='cpf', max_length=30, unique=True, verbose_name='Cpf')),
                ('status_account', models.BooleanField(db_column='status_account', default=False, verbose_name='Status Account')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Account',
                'db_table': 'account',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, db_column='updated_at', verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_column='created_at', verbose_name='Created At')),
                ('description', models.TextField(blank=True, db_column='description', null=True, verbose_name='Description')),
                ('first_name', models.CharField(db_column='first_name', max_length=50, validators=[django.core.validators.RegexValidator(re.compile('[A-Za-z]'), 'Username can only contain letters', 'invalid')], verbose_name='First Name')),
                ('last_name', models.CharField(db_column='last_name', max_length=100, verbose_name='Last Name')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile_user', to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profile',
                'db_table': 'profile',
                'ordering': ['-created_at'],
            },
        ),
        migrations.AddField(
            model_name='user',
            name='account',
            field=models.ManyToManyField(related_name='user_account', to='accounts.Account', verbose_name='Account'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
