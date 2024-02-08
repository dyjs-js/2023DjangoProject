from django.db import models
from django.conf import settings
from common.models import CommonModel
from django.db.models import Avg

# Create your models here.
# room.owner.username
# user.rooms
# user.reviews


class Room(CommonModel):

    """Room model Definition"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHRAED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(
        max_length=180,
        default="",
    )
    country = models.CharField(
        max_length=50,
        default="한국",
    )
    city = models.CharField(
        max_length=80,
        default="경기",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveBigIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="rooms",
    )
    amenities = models.ManyToManyField(
        "rooms.Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="rooms",
    )

    def __str__(self) -> str:
        return self.name

    # def total_amenities(self):
    #     return self.amenities.count()

    # # 여기서 reviews는 related name 사용안하면 review_set 사용
    # def rating(room):
    #     count = room.reviews.count()
    #     if count == 0:
    #         return "No reviews"
    #     else:
    #         total_rating = 0
    #         # print(room.reviews.all().values("rating"))
    #         # print(room.reviews.all())
    #         # <QuerySet [{'rating': 5}, {'rating': 4}, {'rating': 2}, {'rating': 1}]> 를 받게됨
    #         for review in room.reviews.all().values("rating"):
    #             total_rating += review["rating"]
    #         return round(total_rating / count)

    # rating 함수 최적화
    def rating(self):
        average_rating = self.reviews.aggregate(Avg("rating"))["rating__avg"]
        if average_rating is None:
            return "No Reviews"
        else:
            return round(average_rating, 2)


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(
        max_length=150,
    )
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    # 잘못된 스펠링 고치기 Amenitys->Amenities
    class Meta:
        verbose_name_plural = "Amenities"
