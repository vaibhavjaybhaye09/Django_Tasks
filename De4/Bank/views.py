from django.shortcuts import render, redirect, get_object_or_404
from .forms import BankAccountForm
from .models import BankAccount
from django.contrib import messages

def profile(request):
    accounts = BankAccount.objects.all()
    return render(request, 'profile.html', {'accounts': accounts})

def ac_create(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error creating account. Please try again.')
    else:
        form = BankAccountForm()
    return render(request, 'ac_create.html', {'form': form})

def ac_update(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)  # Better error handling
    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Error updating account. Please try again.')
    else:
        form = BankAccountForm(instance=account)
    # Move this outside the else block
    return render(request, 'ac_update.html', {'form': form, 'account': account})
    
def ac_delete(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)  # Better error handling
    if request.method == 'POST':
        account.delete()
        messages.success(request, 'Account deleted successfully!')
        return redirect('profile')
    # Add GET request handling for confirmation page
    return render(request, 'ac_delete.html', {'account': account})