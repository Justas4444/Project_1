from django.shortcuts import render
from .models import StockSymbol, StockPrediction

# Create your views here.

def predictions_view(request):
    # Fetch the stock symbols from the database
    stock_symbols = StockSymbol.objects.all()

    # Fetch the predictions for the selected stock symbol (assuming symbol is passed as a GET parameter)
    selected_symbol = request.GET.get('symbol')
    if selected_symbol:
        predictions = StockPrediction.objects.filter(stock_symbol__symbol=selected_symbol)
    else:
        predictions = None

    # Prepare context data to pass to the template
    context = {
        'stock_symbols': stock_symbols,
        'selected_symbol': selected_symbol,
        'predictions': predictions,
    }

    return render(request, 'predictions.html', context)
