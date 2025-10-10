from django.db import models
import random
import string

class BankAccount(models.Model):
    ACCOUNT_TYPES = (
        ('SAVINGS', 'Savings'),
        ('CHECKING', 'Checking'),
        ('CURRENT', 'Current'),
    )
    
    username = models.CharField(max_length=100, blank=False)
    phone_no = models.CharField(max_length=15, blank=False)
    email = models.EmailField(max_length=100, blank=False)
    photo = models.ImageField(upload_to='images/', blank=False)
    ac_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default='SAVINGS')
    account_number = models.CharField(max_length=12, unique=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def generate_account_number(self):
        """Generate a unique 12-digit account number."""
        return ''.join(random.choices(string.digits, k=12))

    def save(self, *args, **kwargs):
        """Auto-generate account number if not set."""
        if not self.account_number:
            self.account_number = self.generate_account_number()
            # Ensure uniqueness
            while BankAccount.objects.filter(account_number=self.account_number).exists():
                self.account_number = self.generate_account_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username   # ✅ Fixed

    class Meta:
        ordering = ['username']   # ✅ Fixed
