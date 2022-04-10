from django.contrib import admin
from .models import Market, SymbolInfo


class MarketAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name',)
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = '-пусто-'


admin.site.register(Market, MarketAdmin)


class SymbolInfoAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'market', 'lot_size')
    list_editable = ('market',)
    search_fields = ('name',)
    list_filter = ('market',)
    empty_value_display = '-пусто-'


admin.site.register(SymbolInfo, SymbolInfoAdmin)
