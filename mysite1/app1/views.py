from django.core.paginator import Paginator
from django.shortcuts import render
from .models import StockSymbol, StockPrediction

# Create your views here.

def predictions_view(request):
    stock_symbols = StockSymbol.objects.all()
    selected_symbol = request.GET.get('symbol')
    paginate_by = 25  # Adjust this as needed

    if selected_symbol:
        predictions = StockPrediction.objects.filter(stock_symbol__symbol=selected_symbol)
        paginator = Paginator(predictions, paginate_by)
        page_number = request.GET.get('page')
        page = paginator.get_page(page_number)
    else:
        page = None

    context = {
        'stock_symbols': stock_symbols,
        'selected_symbol': selected_symbol,
        'page': page,  # Pass the 'page' object instead of 'predictions'
    }
    return render(request, 'predictions.html', context)

def homepage_view(request):
    return render(request, 'homepage.html')  # Render the homepage template