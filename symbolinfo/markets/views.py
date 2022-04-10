from django.shortcuts import render, get_object_or_404

from .models import Market, SymbolInfo

SYMBOLS_PER_PAGE = 10


def index(request):
    template = 'markets/index.html'
    symbol_infos = SymbolInfo.objects.order_by('name')[:SYMBOLS_PER_PAGE]
    context = {
        'symbol_infos': symbol_infos
    }
    return render(request, template, context)


def market(request, name):
    template = 'markets/market.html'
    market = get_object_or_404(Market, name=name)
    symbol_infos = market.symbols.all().order_by('name')
    context = {
        'market': market,
        'symbol_infos': symbol_infos
    }
    return render(request, template, context)
