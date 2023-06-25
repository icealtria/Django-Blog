from django.utils.html import format_html
from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import reverse

from .models import Post, Category, Tag
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "owner", "post_count"]
    fields = ["name", "owner"]

    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)
    
    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = "文章数量"

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    fields = ["name"]
    
    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)

class CategoryOwnerFilter(admin.SimpleListFilter):
    title = "分类所有者"
    parameter_name = "owner_category"

    def lookups(self, request, model_admin):
        return Category.objects.all().values_list("id", 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(owner=request.user)
        return queryset

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "operator"]
    list_display_links = ["title"]
    
    list_filter = [CategoryOwnerFilter]
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
    
    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css",)
        }
        js = ("https://cdn.bootcss.com/bootstrap/4.0.0/js/bootstrap.bundle.js",)