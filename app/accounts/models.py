import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, UserManager)



class DefaultFieldsModel(models.Model):
    
    updated_at = models.DateTimeField(verbose_name=u'Updated At', auto_now=True, db_column='updated_at')
    created_at = models.DateTimeField(verbose_name=u'Created At', auto_now_add=True, db_column='created_at')
    description = models.TextField(db_column='description', blank=True, null=True, verbose_name=u'Description')

    class Meta:
        abstract = True



class Account(DefaultFieldsModel):

    cpf = models.CharField(max_length=30, verbose_name=u'Cpf', db_column='cpf', unique=True)
    status_account = models.BooleanField(verbose_name=u'Status Account', default=False, db_column='status_account')

    def __str__(self):
        return f'{self.cpf}'

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Account'
        ordering=['-created_at']
        db_table='account'



class UserManager(models.Manager):

    def get_by_natural_key(self, email):
        return self.get(email=email)

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save()
        return user

    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=email,
        )

        user.set_password(password)
        user.save()
        return user

    def create_staffuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_active
        user.save()
        return user



class User(AbstractBaseUser, PermissionsMixin):

    USERNAME_FIELD = 'email'

    username = models.CharField(
        verbose_name=u'Username', max_length=30,
        validators=[validators.RegexValidator(re.compile('[a-zA-Z]'),
            'The username can only contain letters, digits or the '
            'following characters: @/./+/-/_', 'invalid')]
    )
    
    email = models.EmailField(verbose_name=u'E-mail', unique=True)
    is_active = models.BooleanField(verbose_name=u'Active Status', default=False)
    is_staff = models.BooleanField(verbose_name=u'Staff Status', default=False)
    date_joined = models.DateTimeField(verbose_name=u'Date Joined', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=u'Updated At', auto_now=True, db_column='updated_at')
    account = models.ManyToManyField(Account, verbose_name='Account', related_name='user_account')
    objects = UserManager()


    def __str__(self):
        return f'{self.email}'


    def __unicode__(self):
        return f'{self.email}'

    def natural_key(self):
        return (self.email)

    @property
    def name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return str(self)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'User'
        ordering = ['-date_joined']
        db_table='user'



class Profile(DefaultFieldsModel):

    first_name = models.CharField(max_length=50, verbose_name=u'First Name', db_column='first_name', 
                                    validators=[validators.RegexValidator(re.compile('[A-Za-z]'),
                                             	'Username can only contain letters', 'invalid')])
    last_name = models.CharField(max_length=100, verbose_name=u'Last Name', db_column='last_name')
    user = models.OneToOneField(User, verbose_name='Username', related_name='profile_user',
                                	    on_delete=models.CASCADE, null=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
        ordering=['-created_at']
        db_table='profile'
