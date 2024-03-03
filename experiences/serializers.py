from rest_framework.serializers import ModelSerializer
from .models import Perk, Experience
from categories.serializers import CategorySerializer
from users.serializers import TinyUserSerializer


class PerkSerializer(ModelSerializer):
    class Meta:
        model = Perk
        fields = (
            "pk",
            "name",
            "detail",
            "description",
        )


class ExperienceListSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Experience
        exclude = ("created_at", "updated_at", "perks")


class ExperienceDetailSerializer(ModelSerializer):
    host = TinyUserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    perks = PerkSerializer(
        read_only=True,
        many=True,
    )

    class Meta:
        model = Experience
        fields = "__all__"
