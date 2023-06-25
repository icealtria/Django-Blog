from django.utils.html import format_html
from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import reverse

from .models import Post, Category, Tag

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "owner"]
    fields = ["name", "owner"]

    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "operator"]
    list_display_links = ["title"]
    
    list_filter = ["category", "tags"]
    search_fields = ["title", "catagory__name", "tags__name"]
    
    actions_on_top = True
        
    fields = ["title", "category", "tags", "body"]
    
    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse("admin:blog_post_change", args=(obj.id,)),
        )
    operator.short_description = "操作"
    
    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)