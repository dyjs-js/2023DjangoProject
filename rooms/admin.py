from django.contrib import admin
from .models import Room, Amenity

# Register your models here.


@admin.action(description="Set all prices to zero")
def reset_price(model_admin, request, rooms):
    # print(room) 선택된 room 이름 확인
    for room in rooms.all():
        room.price = 0
        room.save()


# Room model의 admin을 컨트롤
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    actions = (reset_price,)
    list_display = (
        "name",
        "owner",
        "price",
        "total_amenities",
        "rating",
        "kind",
        "created_at",
    )
    list_filter = (
        "country",
        "city",
        "price",
        "rooms",
        "toilets",
        "pet_friendly",
        "kind",
        "amenities",
    )

    # 코드로 데이터베이스에서 데이터를 가져와서 추가하기
    def total_amenities(self, room):
        return room.amenities.count()

    # price는 시작하는 숫자로 검색
    search_fields = (
        "owner__username",
        "name",
        "^price",
    )


# Amenity model의 admin을 컨트롤
@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "created_at",
        "updated_at",
    )
    readonly_fields = (
        "created_at",
        "updated_at",
    )
