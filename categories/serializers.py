from rest_framework import serializers
from .models import Category


# serializer에게 카테고리 필드 중에 어떤 부분을 보여줄지 명시
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            "name",
            "kind",
        )
        # or exclude로 할 수도있음 (제외)
        # fields = "__all__" 모든 필드 보여주기
