from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, username, email, phone_number, password=None):
        if not username:
            raise ValueError('User must have username')

        if not phone_number:
            raise ValueError('Phone number needed')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,

        )
        user.is_customer = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_customer(self, username, email, phone_number,password):
        if not username:
            raise ValueError('User must have username')

        if not phone_number:
            raise ValueError('Phone number needed')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )
        user.is_customer = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone_number, password):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_manager(self, username, email, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )
        user.role = "MANAGER"
        user.is_customer = False
        user.is_staff = True
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_front_desk(self, username, email, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )
        user.is_customer = False
        user.role = "FRONT-DESK"
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_advisor(self, username, email, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            phone_number=phone_number,
        )
        user.is_customer = False
        user.role = "ADVISOR"

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_mechanic(self, username, email, phone_number, password=None):
        user = self.model(
            email=self.normalize_email(email),
            username=username,

            phone_number=phone_number,
        )
        user.is_customer = False
        user.role = "MECHANIC"
        user.set_password(password)
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    STATUS = (
        ('MANAGER', 'MANAGER'),
        ('ADVISOR', 'ADVISOR'),
        ('MECHANIC', 'MECHANIC'),
        ('FRONT-DESK', 'FRONT-DESK')
    )

    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50, unique=True)
    address = models.TextField(max_length=200, default="")

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_customer = models.BooleanField(default=False)
    role = models.CharField(max_length=100, null=True, choices=STATUS)
    is_pda = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone_number', 'email', ]

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True
