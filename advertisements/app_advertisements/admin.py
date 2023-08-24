from django.contrib import admin
from .models import Advertisement
from datetime import datetime
from django.utils.html import format_html

class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id','title','description', 'price','created_at','updated_at', 'get_updated_at_display','auction','image']
    list_filter = ['auction','created_at']
    actions = ['make_auction_false','make_auction_true']
    fieldsets = [
        ("Общее", {'fields': ['title','description','image']}),
        ("Финансы", {'fields': ['price','auction'], "classes": ['collapse']}),
    ]
    @admin.action(description="Убрать возможность торга")
    def make_auction_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description="Поставить возможность торга")
    def make_auction_true(self, request, queryset):
        queryset.update(auction=True)

    def get_updated_at_display(self, obj):
        updated_at = obj.updated_at
        today = datetime.now().date()
        if updated_at.date() == today:
            return format_html('<span style="color:purple;">Сегодня в {}</span>', updated_at.time())
        else:
            return str(updated_at)
    get_updated_at_display.short_description = 'Последнее обновление'
    get_updated_at_display.allow_tags = True

admin.site.register(Advertisement, AdvertisementAdmin)
# Register your models here.
