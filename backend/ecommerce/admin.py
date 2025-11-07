from django.contrib import admin
from . import models


@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'stock')
    search_fields = ('title',)
    list_filter = ('price','stock')
    readonly_fields = ('id',)
    ordering = ('title',)  # sorts alphabetically


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'quantity')
    search_fields = ('item__title',)
    list_filter = ('item',)
    ordering = ('id',)