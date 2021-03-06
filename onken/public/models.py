from django.db import models
from django_tenants.models import TenantMixin, DomainMixin
from django.contrib.auth.models import AbstractUser


class Workspace(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Domain(DomainMixin):
    def __str__(self):
        return self.domain


class User(AbstractUser):
    pass
