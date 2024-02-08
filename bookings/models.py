from django.db import models
from django.conf import settings
from common.models import CommonModel

# Create your models here.


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    kind = models.CharField(
        max_length=15,
        choices=BookingKindChoices,
    )
    # booking은 한개의 유저를 가고있고, 유저는 여러개의 예약들을 가질 수 있음
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,  # user가 삭제되면 예약도 삭제되어야함
        related_name="bookings",
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # 방이 지워지면 set null
        related_name="bookings",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,  # experience 지워지면 set null
        related_name="bookings",
    )

    check_in = models.DateField(
        null=True,  # experience를 할때는 체크인 체크아웃이 필요없기 때문
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    experience_time = models.DateTimeField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} booking for {self.user}"
