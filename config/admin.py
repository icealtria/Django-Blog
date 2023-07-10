from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from .models import Link, SideBar, Nav

# Register your models here.


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ["title", "href", "status"]
    fields = ["title", "href", "status", "weight"]

    def save_model(
        self, request: HttpRequest, obj: Any, form: Any, change: Any
    ) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(SideBar)
class SideBarAdmin(admin.ModelAdmin):
    list_display = ["title", "display_type", "content", "status"]
    fields = ["title", "display_type", "content", "status"]

    def save_model(
        self, request: HttpRequest, obj: Any, form: Any, change: Any
    ) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

@admin.register(Nav)
class NavAdmin(admin.ModelAdmin):
    list_display = ["title", "link", "status"]
    fields = ["title", "link", "status"]
