# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_test_51HXIn5IXMf2O3DadrtYI7Gpuf3tcVxC1Wpkwll0OL0I3LpXuAxXukg6P7OksH7zhq4zOzd3LURZ6FFdZcm9l64Vi00weEBWSdt"

# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['nickname'],
			source=request.POST['stripeToken']
			)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='inr',
			description="Donation"
			)

	return redirect(reverse('success', args=[amount]))

def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})