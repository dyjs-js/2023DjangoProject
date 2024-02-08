from django.db import models
from django.conf import settings
from common.models import CommonModel

# Create your models here.


# 두개의 class room이 둘다 user model을 사용하기 때문에 에러가 발생
class ChattingRoom(CommonModel):

    """Room Model Definition"""

    users = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="chattingrooms",
    )

    def __str__(self) -> str:
        return "Chatting room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="messages",
    )

    room = models.ForeignKey(
        "direct_messages.ChattingRoom",
        on_delete=models.CASCADE,
        related_name="messages",
    )

    def __str__(self) -> str:
        return f"{self.user} says: {self.text}"
