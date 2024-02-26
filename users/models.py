from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    class Genderchoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        En = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollor")

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    name = models.CharField(
        max_length=150,
        default="",
    )
    is_host = models.BooleanField(
        default=False,
    )
    avatar = models.URLField(blank=True)  # 필드를 비어놓을 수 있도록 blank = True
    gender = models.CharField(
        max_length=10,
        choices=Genderchoices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices,
    )
