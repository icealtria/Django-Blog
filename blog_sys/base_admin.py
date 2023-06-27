from typing import Any
from django.contrib import admin
from django.http.request import HttpRequest

class BaseOwnerAdmin(admin.ModelAdmin):
    
    exclude = ('owner',)
    
    def queryset(self, request, queryset):
        qs = super(BaseOwnerAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)
    
    def save_model(self, request: HttpRequest, obj: Any, form: Any, change: Any) -> None:
        obj.owner = request.user
        return super().save_model(request, obj, form, change)