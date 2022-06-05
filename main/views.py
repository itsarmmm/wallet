from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
import pytz
from .models import Account, Orders

# Create your views here.


def get_part_of_day(h):
    return (
        "morning"
        if 5 <= h <= 11
        else "afternoon"
        if 12 <= h <= 17
        else "evening"
        if 18 <= h <= 22
        else "night"
    )


def index(request):
    return render(request, 'main/index.html')


def auth(request):
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    hour = now.strftime("%H")

    day_part = get_part_of_day(int(hour))

    status = 0
    if request.user.is_authenticated:
        print(1)
        return redirect('profile')

    if 'username' and 'password' in request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            status = 'logged'
            login(request, user)
            return redirect('profile')
        else:
            status = 'error'

    data = {
        'status': status,
        'day_part': day_part
    }
    print(day_part)
    print(hour)
    return render(request, 'main/auth.html', data)


def mobile(request):

    return render(request, 'main/mobile.html')


@login_required
def profile(request):
    now = datetime.now(pytz.timezone('Europe/Moscow'))
    hour = now.strftime("%H")
    status = 0

    account = Account.objects.get(user_id=request.user.id)
    day_part = get_part_of_day(int(hour))

    if 'amount' and 'address' in request.POST:
        user_balance = float(Account.objects.filter(user_id=request.user.id).values_list('balance')[0][0])
        Orders.objects.create(user_id=request.user.id, username=request.user.username,
                              amount=request.POST['amount'], address=request.POST['address'])

        user_balance = user_balance - float(request.POST['amount'])
        Account.objects.filter(user_id=request.user.id).update(balance=user_balance)
        status = 1

    data = {
        'day_part': day_part,
        'account': account,
        'status': status
    }

    return render(request, 'main/profile.html', data)


@login_required
def sign_out(request):
    logout(request)
    return redirect('auth')
