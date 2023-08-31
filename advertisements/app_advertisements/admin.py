from django.contrib import admin
from .models import Advertisement

# Register your models here.


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date', 'updated_date', 'auction', 'user', 'get_html_image']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false']
    fieldsets = (
        ('Общее ', {
            'fields': ('title', 'description', 'user', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
        })
    )
    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, requests, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

admin.site.register(Advertisement, AdvertisementAdmin)