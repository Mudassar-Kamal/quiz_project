from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
# from django.urls import reverse
from accounts.managers import CustomUserManager
# from django.contrib.auth.validators import UnicodeUsernameValidator

SUPER_ADMIN = 'super_admin'
STUDENT = 'student'
class User(AbstractUser):
    # username_validator = UnicodeUsernameValidator()
    ROLES = (
        (SUPER_ADMIN, 'Super_Admin'),
        (STUDENT, 'Student'),
    )
    user_type = models.CharField(max_length=100, choices=ROLES, default=SUPER_ADMIN)
    roll_number = models.CharField(max_length=100,blank=True, null=True)
    username = models.CharField(unique=True, max_length=100, blank=True, null=True)
    grade = models.CharField( max_length=100, blank=True, null=True)
    group_name = models.CharField( max_length=100, blank=True, null=True)
    category = models.CharField( max_length=100, blank=True, null=True)
    school_name = models.CharField(max_length=200, blank=True, null=True)
    campus_name = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField( max_length=100, blank=True, null=True)
    school_code = models.CharField( max_length=100, blank=True, null=True)
    full_address = models.CharField( max_length=100, blank=True, null=True)
    code = models.CharField( max_length=100, blank=True, null=True)
    readable_password = models.CharField(max_length=100, blank=True, null=True)
    active_user = models.BooleanField(default=True)



    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username