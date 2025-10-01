from django.shortcuts import render, redirect, get_object_or_404
from .forms import BankAccountForm
from .models import BankAccount
from django.contrib import messages

# Show one account
def profile_list(request):
    accounts = BankAccount.objects.all()
    return render(request, 'Bank/profile_list.html',{'accounts':accounts})


def profile(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    return render(request, 'Bank/profile.html', {'account': account})

# Create new account
def ac_create(request):
    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES)
        if form.is_valid():
            account = form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('profile', pk=account.pk)   # ✅ go to detail
        else:
            messages.error(request, 'Error creating account. Please try again.')
    else:
        form = BankAccountForm()
    return render(request, 'Bank/ac_create.html', {'form': form})

# Update account
def ac_update(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    if request.method == 'POST':
        form = BankAccountForm(request.POST, request.FILES, instance=account)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account updated successfully!')
            return redirect('profile', pk=account.pk)   # ✅ go to detail
        else:
            messages.error(request, 'Error updating account. Please try again.')
    else:
        form = BankAccountForm(instance=account)
    return render(request, 'Bank/ac_update.html', {'form': form, 'account': account})

# Delete account

def ac_delete(request, pk):
    account = get_object_or_404(BankAccount, pk=pk)
    account.delete()
    return redirect('profile_list')
