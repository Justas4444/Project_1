from django.core.paginator import Paginator
from django.shortcuts import render
from .models import StockSymbol, StockPrediction
from django.shortcuts import redirect
from django.contrib.auth.forms import User
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

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
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1
    context = {
        'num_visits': num_visits,
    }
    return render(request, 'homepage.html', context=context)  # Render the homepage template

@csrf_protect
def register(request):
    if request.method == "POST":
        # Get values from the registration form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # Check if passwords match
        if password == password2:
            # Check if the username is taken
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Username {username} is already taken!')
                return redirect('register')
            else:
                # Check if the email is already registered
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'A user with the email {email} is already registered!')
                    return redirect('register')
                else:
                    # If everything is okay, create a new user
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, f'User {username} has been registered!')
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
    return render(request, 'register.html')

@login_required
def profile(request):
    return render(request, 'profile.html')
