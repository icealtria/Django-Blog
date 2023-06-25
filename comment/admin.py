from django.contrib import admin
from .models import Comment
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["name", "post", "email", "body", "created", "active"]
    list_filter = ["active", "created"]
    search_fields = ["name", "email", "body"]
    actions_on_top = True