from django.contrib import admin
from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "client_type", "industry", "account_manager", "portal_enabled")
    list_filter = ("status", "client_type", "portal_enabled")
    search_fields = ("name", "trading_name", "industry", "city")
    raw_id_fields = ("account_manager",)
