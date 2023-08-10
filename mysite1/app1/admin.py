from django.contrib import admin
from .models import StockSymbol, StockPrediction

# Register your models here.

class StockSymbolAdmin(admin.ModelAdmin):
    list_display = ('symbol', 'company_name')
    search_fields = ('symbol', 'company_name')

class StockPredictionAdmin(admin.ModelAdmin):
    list_display = ('stock_symbol', 'predicted_date', 'predicted_open', 'predicted_high', 'predicted_low', 'predicted_close', 'predicted_adjclose', 'predicted_volume', 'predicted_interest_rate')
    list_filter = ('stock_symbol', 'predicted_date')
    search_fields = ('stock_symbol__symbol', 'predicted_date')
    ordering = ('stock_symbol', 'predicted_date')

admin.site.register(StockSymbol, StockSymbolAdmin)
admin.site.register(StockPrediction, StockPredictionAdmin)