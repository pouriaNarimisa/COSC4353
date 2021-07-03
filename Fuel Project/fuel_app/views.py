from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.forms import modelform_factory
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import QuoteForm, ProfileForm
from .models import Client, Quote

# homepage view
def index(request):
    return render(request, 'index.html')

# registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, './registration/register.html', {'form': form})

# fuel quote form view
@login_required
def quote(request):
    current_client = Client.objects.filter(user=request.user).first()
    # if the current user has not updated their client profile, return error page directing them to do so
    if not current_client:
        return render(request, 'quote_error.html')
    quote_count = Quote.objects.filter(user=request.user).count()
    if request.method == 'POST' and request.user.is_authenticated:
        form = QuoteForm(request.POST)
        if form.is_valid():
            price = form.cleaned_data.get('price')
            date = form.cleaned_data.get('date')
            address = form.cleaned_data.get('address')
            gallons = form.cleaned_data.get('gallons')
            total_price = form.cleaned_data.get('total_price')
            new_quote = Quote(user=request.user, price=price, date=date, address=address,
                gallons=gallons, total_price=total_price)
            new_quote.save()
            return HttpResponseRedirect('/history')
        else:
            form = QuoteForm()
    else:
        form = QuoteForm()
    return render(request, 'quote.html', {'form': form, 'current_profile': current_client, 'quote_count': quote_count})

# fuel quote history view
@login_required
def history(request):
    fuel_quote = Quote.objects.all().filter(user=request.user).order_by('-id')
    return render(request, 'history.html', {'fuel_quote': fuel_quote})

# profile management view
@login_required
def profile(request):
    current_client = Client.objects.filter(user=request.user).first()
    if request.method == 'POST' and request.user.is_authenticated:
        form = ProfileForm(request.POST)
        if form.is_valid():
            c_name = form.cleaned_data.get('name')
            c_address = form.cleaned_data.get('address_1')
            c_city = form.cleaned_data.get('city')
            c_state = form.cleaned_data.get('state')
            c_zipcode = form.cleaned_data.get('zipcode')
            obj, created = Client.objects.update_or_create(user=request.user,
                defaults={'name': c_name, 'address': c_address, 'city': c_city,
                'state': c_state, 'zipcode': c_zipcode})
            return HttpResponseRedirect('/profile')
        else:
            form = ProfileForm()
    else:
        form = ProfileForm()
    return render(request, 'profile.html', {'form': form, 'current_profile': current_client})