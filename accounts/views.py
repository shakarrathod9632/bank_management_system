from django.shortcuts import render, get_object_or_404, redirect
from .models import Account

def menu(request):
    accounts = Account.objects.all()
    return render(request, 'menu.html', {'accounts': accounts})

def deposit(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        account.deposit(amount)
        return redirect('menu')
    return render(request, 'deposit.html', {'account': account})

def withdraw(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    message = ""
    if request.method == 'POST':
        amount = float(request.POST.get('amount'))
        success = account.withdraw(amount)
        if not success:
            message = "❌ Insufficient Balance!"
        return redirect('menu')
    return render(request, 'withdraw.html', {'account': account, 'message': message})


