from django.db import models


# Create your models here.
class UserRoles(models.TextChoices):
    ADMIN = "admin", "Admin"
    AGENCY = "agency", "Agency"
    USER = "user", "User"


class MemberShip(models.TextChoices):
    FREE = "free", "Free"
    PRO = "premium", "Premium"
    VIP = "vip", "VIP"


class User(models.Model):
    name = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField()
    role = models.CharField( choices=UserRoles.choices, default=UserRoles.USER)
    membership = models.CharField(choices=MemberShip.choices, default=MemberShip.FREE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name

