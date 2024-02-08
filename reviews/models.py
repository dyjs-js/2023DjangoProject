from django.db import models
from common.models import CommonModel
from django.conf import settings
from django.core.validators import MaxValueValidator

# Create your models here.


class Review(CommonModel):
    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )
    # 리뷰는 하나의 experience를 가지고 , experience는 많은 reviews를 가질 수 있음
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="reviews",
    )

    payload = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[MaxValueValidator(5)],
    )  # 최대 별점 5로 설정

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
