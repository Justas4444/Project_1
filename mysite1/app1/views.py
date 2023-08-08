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

def index(request):
    num_spx_predictions = StockPrediction.objects.filter.filter(stock_symbol__symbol="SPX - S&P 500 INDEX") 
    num_ndx_predictions = StockPrediction.objects.filter.filter(stock_symbol__symbol="NDX - Nasdaq-100") 
    num_symbols = StockSymbol.objects.all().count()

    context = {
        'num_spx_predictions': num_spx_predictions,
        'num_ndx_predictions': num_ndx_predictions,
        'num_symbols': num_symbols,
    }

    return render(request, 'index.html', context=context)


from django.shortcuts import render

def homepage_view(request):
    return render(request, 'homepage.html')  # Render the homepage template
