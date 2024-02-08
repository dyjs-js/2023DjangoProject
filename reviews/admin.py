from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from .models import Review


class GoodOrBadFilter(admin.SimpleListFilter):
    title = "Filter by Good or Bad !"
    parameter_name = "word"

    def lookups(self, request, model_admin):
        return [
            ("good", "Good"),
            ("bad", "Bad"),
        ]

    def queryset(self, request, reviews):
        word = self.value()
        if word:
            return reviews.filter(payload__contains=word)
        else:
            reviews


# Register your models here.
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "__str__",
        "payload",
    )

    list_filter = (
        GoodOrBadFilter,
        "rating",
        "user__is_host",
        "room__category",  # ForeignKey 라서 가능
        "room__pet_friendly",
    )
